# Requirements
# Print a random string every 5 seconds with timestamp

import datetime, random, string, time,logging,os,threading
from flask import Flask , render_template

HASH_STRING = ""

def generate_random_log():
    global HASH_STRING
    while True:
        rstr = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
        timestamp = datetime.datetime.now()
        HASH_STRING = f"{timestamp} {rstr}"
        print(HASH_STRING)
        time.sleep(5)


logging.getLogger('werkzeug').setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/')
def index():
    return f"{HASH_STRING}"

if __name__ == "__main__":
    threading.Thread(target=generate_random_log, daemon=True).start()
    port = os.environ.get("PORT","5000")
    print(f"The Server started at {port}")
    app.run(host="0.0.0.0",port=int(port), debug=True)
