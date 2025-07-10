# Requirements
# Print a random string every 5 seconds with timestamp

import datetime, random, string, time
rstr = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
while True:
    timestamp = datetime.datetime.now()
    print(f"{timestamp} {rstr}")
    time.sleep(5)
