import os
import time


print(os.popen("wrk -t32 -c250 -d5m -s WRK-report2.lua --latency http://0.0.0.0:80/get").read())
time.sleep(60)