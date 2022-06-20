import os
import time


print(os.popen('wrk -t32 -c500 -d5m -s WRK-report9.lua --timeout 5m --latency \"http://0.0.0.0:80/drip?numbytes=5000&delay=0&duration=0&status=200\"'))
time.sleep(60)