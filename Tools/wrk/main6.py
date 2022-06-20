import os
import time


print(os.popen("wrk -t32 -c500 -d5m -s WRK-report6.lua --latency http://0.0.0.0:80/stream/100").read())
time.sleep(60)