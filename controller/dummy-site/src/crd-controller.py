import threading
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import kopf

HOST_NAME = "0.0.0.0"
SERVER_PORT = 8080
HTML_CONTENT = "No content"


def get_site(web_url: str):
    global HTML_CONTENT
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    resp = requests.get(web_url, timeout=10, headers=headers)
    resp.raise_for_status()
    HTML_CONTENT = resp.text


class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(HTML_CONTENT.encode("utf-8"))

    def log_message(self, format, *args):
        return


def start_http_server():
    server = HTTPServer((HOST_NAME, SERVER_PORT), DummyHandler)
    server.serve_forever()


@kopf.on.startup()
def _startup(logger, **kwargs):
    t = threading.Thread(target=start_http_server, daemon=True)
    t.start()
    logger.info("Started HTTP server thread.")


@kopf.on.create("dummysites")
def clone(spec, name, namespace, logger, **kwargs):
    web_url = spec.get("website_url")
    if not web_url:
        raise kopf.PermanentError(f"An URL must be set, got: {web_url!r}")

    logger.info(f"Fetching site for DummySite {namespace}/{name}: {web_url!r}")

    try:
        get_site(web_url)
        logger.info("Site cloned into memory successfully.")
    except Exception as e:
        logger.error(f"Failed to fetch site {web_url!r}: {e}")
        raise

@kopf.on.delete("dummysites")
def on_delete_dummysite(spec, name, namespace, logger, **kwargs):
    global HTML_CONTENT
    HTML_CONTENT = "No content"
