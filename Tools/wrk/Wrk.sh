wrk -t32 -c32 -d5m -s WRK-report1.lua --latency http://0.0.0.0:80/get

wrk -t32 -c250 -d5m -s WRK-report2.lua --latency http://0.0.0.0:80/get

wrk -t32 -c500 -d5m -s WRK-report3.lua --latency http://0.0.0.0:80/get

wrk -t32 -c32 -d5m -s WRK-report4.lua --latency http://0.0.0.0:80/stream/100

wrk -t32 -c250 -d5m -s WRK-report5.lua --latency http://0.0.0.0:80/stream/100

wrk -t32 -c500 -d5m -s WRK-report6.lua --latency http://0.0.0.0:80/stream/100

wrk -t32 -c32 -d5m -s WRK-report7.lua --latency http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0

wrk -t32 -c250 -d5m -s WRK-report8.lua --latency http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0

wrk -t32 -c500 -d5m -s WRK-report9.lua --latency http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0
