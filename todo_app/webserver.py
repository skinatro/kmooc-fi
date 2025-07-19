from flask import Flask
import logging, os

logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    print(f"Server started on port: {port}")
    app.run(host="0.0.0.0", port=int(port), debug=False)
