import os
import time


print(os.popen("wrk -t32 -c32 -d5m -s WRK-report4.lua --latency http://0.0.0.0:80/stream/100").read())
time.sleep(60)