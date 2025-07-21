"""
Count the number of the GET requests to the app and store it a file
"""
import os
from flask import Flask, request

app = Flask(__name__)

class Counter:
    """
    Class to increment the number of visits to the site and save to file
    """
    def __init__(self):
        self.value = 0

    def increment(self):
        """
        Method to increment the number of visits to the site and save to file
        """
        # file_path = "/tmp/kube/pongs.txt"
        self.value += 1

        # with open(file_path, 'w') as file:
        #     file.write("ping pongs "+str(self.value) + '\n')
        return self.value

counter = Counter()

@app.route("/pings")
def ping():
    """
    Shows the number of pings
    """
    return str(counter.increment())

@app.route('/pingpong')
def pong():
    """
    Call the increment function to increment and log to file upon GET request
    """
    if request.method == 'GET':
        return f"Ping / Pong: {counter.increment()}"

if __name__ == '__main__':
    PORT = os.environ.get("PORT", "5000")
    app.run(host="0.0.0.0", port=int(PORT), debug=True)
