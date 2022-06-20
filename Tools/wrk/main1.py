import os
import time


print(os.popen("wrk -t32 -c32 -d5m -s WRK-report1.lua --latency http://0.0.0.0:80/get").read())
time.sleep(60)