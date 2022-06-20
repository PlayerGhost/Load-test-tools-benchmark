import os
import time


print(os.popen("wrk -t32 -c250 -d5m -s WRK-report5.lua --latency http://0.0.0.0:80/stream/100").read())
time.sleep(60)