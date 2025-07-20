"""
A simple to do list app
"""
import logging
import os
import time
import urllib.request
from flask import Flask, render_template

logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)

file_name = "/usr/src/app/static/image.jpg"
start_time = 0
timeout = int(os.environ.get("TIMEOUT", "600"))  # 10 min default


def download_file():
    """
    Download file from the source
    """
    global start_time
    with urllib.request.urlopen(url="https://picsum.photos/1200") as response, open(file_name, 'wb') as out_file:
        out_file.write(response.read())
    start_time = time.time()


def download_new():
    """
    Check if refresh needed
    """
    return time.time() - start_time > timeout


@app.route("/")
def index():
    """
    Serve the webpage
    """
    if download_new():
        download_file()
    return render_template("index.html")


if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    print(f"Server started on port: {port}")
    app.run(host="0.0.0.0", port=int(port), debug=False)
