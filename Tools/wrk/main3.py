import os
import time


print(os.popen("wrk -t32 -c500 -d5m -s WRK-report3.lua --latency http://0.0.0.0:80/get").read())
time.sleep(60)