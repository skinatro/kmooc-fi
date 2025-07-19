"""Read Log from a file and server it"""

import logging
import os
from flask import Flask

logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/')
def index():
    """
    Read the logs created by the generator and serve it on endpoin /
    """
    
    file_path = "/usr/src/app/files/logs.txt"
    
    with open(file_path,'r') as file:
        return f"{file.read()}"

if __name__ == "__main__":
    port = os.environ.get("PORT","5000")
    print(f"The Server started at {port}")
    app.run(host="0.0.0.0",port=int(port), debug=True)
