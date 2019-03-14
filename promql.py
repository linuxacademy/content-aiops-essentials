import requests
import time
import sys

# Prometheus api endpoint for query 
URL = "http://localhost:9090/api/v1/query"

# Memory Query
PROMQL1 = {'query':'(node_memory_MemTotal_bytes - (node_memory_MemFree_bytes + node_memory_Cached_bytes + node_memory_Buffers_bytes)) / node_memory_MemTotal_bytes * 100'}

# CPU Query
PROMQL2 = {'query':'100 - avg(irate(node_cpu_seconds_total{job="node",mode="idle"}[5m])) by (instance) * 100'}

print("row,instance,memory,cpu")

line_no = 1

#Query every 15 seconds 100 times
for seq in range(0 , 100):
    rows = []
    row = 0

    r1 = requests.get(url = URL, params = PROMQL1)

    r2 = requests.get(url = URL, params = PROMQL2)

    r1_json = r1.json()['data']['result']
    r2_json = r2.json()['data']['result']

    for result in r1_json:
        l = []
        l.append(result['metric'].get('instance', ''))
        l.append(result['value'][1])
        rows.append(l)

    for result in r2_json:
        l = []
        l.append(result['value'][1])
        rows[row].append(l[0])
        row = row + 1

    for ro in rows:
        line = str(line_no)
        line = line + "," + ro[0] + "," + ro[1] + "," + ro[2]
        print(str(line))
        line_no = line_no + 1
    sys.stdout.flush()
    time.sleep(15)
