import os
import time


print(os.system('wrk -t32 -c32 -d5m -s WRK-report7.lua --timeout 5m --latency \"http://0.0.0.0:80/drip?numbytes=5000&delay=0&duration=0&status=200\"'))
time.sleep(60)