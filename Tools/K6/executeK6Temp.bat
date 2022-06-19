#!/usr/bin/env bash

echo "Rota /drip - 900 usuarios"
k6 run src/index.js --summary-export=k69.json -e BASE_URL=LOCAL -e ROUTE=SLOW -e MAX_USERS=900