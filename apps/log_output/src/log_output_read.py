"""Read Log from a file and server it"""

import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Read the logs created by the generator and serve it on endpoin /
    """
    file_path_logs = "/tmp/kube/logs.txt"
    #file_path_pongs = "/tmp/kube/pongs.txt"
    file_path_confmap = "/etc/config/information.txt"

    with open(file_path_confmap,'r') as confmap:
        confmapfile_content = confmap.read()

    envvar_content = os.environ.get("MESSAGE")

    with open(file_path_logs,'r') as logs:
        logs_content = logs.read()
    # with open(file_path_pongs,'r') as pongs:
    #     pongs_content = pongs.read()
    
    with requests.get(url="http://ping-pong-app-svc:5000/pings", timeout=3) as response:
        pongs_content = response.text
        
    return f"file content: {confmapfile_content} <br> env variable: MESSAGE={envvar_content} <br> {logs_content} <br> Ping / Pongs: {pongs_content}"

if __name__ == "__main__":
    port = os.environ.get("PORT")
    print(f"The Server started at {port}")
    app.run(host="0.0.0.0",port=int(port), debug=True)
