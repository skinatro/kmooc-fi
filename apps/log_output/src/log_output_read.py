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
    file_path_logs = "/tmp/kube/logs.txt"
    file_path_pongs = "/tmp/kube/pongs.txt"
    
    with open(file_path_logs,'r') as logs:
        logs_content = logs.read()
    with open(file_path_pongs,'r') as pongs:
        pongs_content = pongs.read()
    return f"{logs_content} {pongs_content}"

if __name__ == "__main__":
    port = os.environ.get("PORT","5000")
    print(f"The Server started at {port}")
    app.run(host="0.0.0.0",port=int(port), debug=True)
