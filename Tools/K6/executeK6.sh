echo "Nova métrica - 500 usuarios"
k6 run src/index-custom.js -e VU=500 --summary-export=new-metric-3.json