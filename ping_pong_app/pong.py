import os, logging
from flask import Flask

logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

counter = Counter()

@app.route('/pingpong')
def pong():
    return f"pong {counter.increment()}"

if __name__ == '__main__':
    PORT = os.environ.get("PORT", "5000")
    app.run(host="0.0.0.0", port=int(PORT), debug=True)
