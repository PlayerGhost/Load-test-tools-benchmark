#!/usr/bin/env bash

echo "Rota /get - 32 usuarios"
k6 run src/index.js --summary-export=k61.json -e BASE_URL=LOCAL -e ROUTE=GET -e MAX_USERS=32 

echo "Rota /get - 250 usuarios"
k6 run src/index.js --summary-export=k62.json -e BASE_URL=LOCAL -e ROUTE=GET -e MAX_USERS=250

echo "Rota /get - 500 usuarios"
k6 run src/index.js --summary-export=k63.json -e BASE_URL=LOCAL -e ROUTE=GET -e MAX_USERS=500

echo "Rota /stream - 32 usuarios"
k6 run src/index.js --summary-export=k64.json -e BASE_URL=LOCAL -e ROUTE=STREAM -e MAX_USERS=32 

echo "Rota /stream - 250 usuarios"
k6 run src/index.js --summary-export=k65.json -e BASE_URL=LOCAL -e ROUTE=STREAM -e MAX_USERS=250

echo "Rota /stream - 500 usuarios"
k6 run src/index.js --summary-export=k66.json -e BASE_URL=LOCAL -e ROUTE=STREAM -e MAX_USERS=500

echo "Rota /drip - 32 usuarios"
k6 run src/index.js --summary-export=k67.json -e BASE_URL=LOCAL -e ROUTE=DRIP -e MAX_USERS=32 

echo "Rota /drip - 250 usuarios"
k6 run src/index.js --summary-export=k68.json -e BASE_URL=LOCAL -e ROUTE=DRIP -e MAX_USERS=250

echo "Rota /drip - 500 usuarios"
k6 run src/index.js --summary-export=k69.json -e BASE_URL=LOCAL -e ROUTE=DRIP -e MAX_USERS=500

echo "Nova métrica - 32 usuarios"
k6 run src/index-custom.js -e VU=32 --summary-export=new-metric-1.json

echo "Nova métrica - 250 usuarios"
k6 run src/index-custom.js -e VU=250 --summary-export=new-metric-2.json

echo "Nova métrica - 500 usuarios"
k6 run src/index-custom.js -e VU=500 --summary-export=new-metric-3.json