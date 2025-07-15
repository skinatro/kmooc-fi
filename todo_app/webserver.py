from flask import Flask
import logging, os

logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    port = os.environ.get("PORT")
    print(f"Server started on port: {port}")
    app.run(port=port, debug=False)
