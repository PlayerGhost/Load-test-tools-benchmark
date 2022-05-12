import os
import time


if __name__ == '__main__':
    print(os.popen("wrk -t32 -c32 -d5m -s WRK-report1.lua --latency http://0.0.0.0:80/get").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c250 -d5m -s WRK-report2.lua --latency http://0.0.0.0:80/get").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c900 -d5m -s WRK-report3.lua --latency http://0.0.0.0:80/get ").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c32 -d5m -s WRK-report4.lua --latency http://0.0.0.0:80/stream/30000").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c250 -d5m -s WRK-report5.lua --latency http://0.0.0.0:80/stream/30000").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c900 -d5m -s WRK-report6.lua --latency http://0.0.0.0:80/stream/30000").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c32 -d5m -s WRK-report7.lua --timeout 5m --latency \"http://0.0.0.0:80/drip?numbytes=10000&delay=0&duration=0&status=200\"").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c250 -d5m -s WRK-report8.lua --timeout 5m --latency \"http://0.0.0.0:80/drip?numbytes=10000&delay=0&duration=0&status=200\"").read())
    time.sleep(60)

    print(os.popen("wrk -t32 -c900 -d5m -s WRK-report9.lua --timeout 5m --latency \"http://0.0.0.0:80/drip?numbytes=10000&delay=0&duration=0&status=200\"").read())
    time.sleep(60)
