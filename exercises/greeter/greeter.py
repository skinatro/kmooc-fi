import os
from flask import Flask, Response, request

app = Flask(__name__)

greet = os.environ.get("GREET", "Hello")
version_no = os.environ.get("VERNO", "1")



@app.route('/healthz')
def healthz():
    """
    Health check endpoint.
    Simple check returning 200 OK.
    """
    return Response("OK", status=200)


@app.route('/')
def index():
    """
    GET return a greeting with version number
    """
    if request.method == 'GET':
        return (f"greeting: {greet} from {version_no}")
    
if __name__ == "__main__":
    port = os.environ.get("PORT", "5000")
    print(f"The Server started at {port}")
    app.run(host="0.0.0.0", port=int(port), debug=True)
