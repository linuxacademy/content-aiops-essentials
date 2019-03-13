import csv
import requests
import sys

# Prometheus api endpoint for query 
URL = "http://localhost:9090/api/v1/query"

# Memory query
PROMQL1 = {'query':'(node_memory_MemTotal_bytes - (node_memory_MemFree_bytes + node_memory_Cached_bytes + node_memory_Buffers_bytes)) / node_memory_MemTotal_bytes * 100'}

# CPU Query
PROMQL2 = {'query':'100 - avg(irate(node_cpu_seconds_total{job="node",mode="idle"}[5m])) by (instance) * 100'}

# sending get request and saving the response as response object 
r1 = requests.get(url = URL, params = PROMQL1)
memry = r1.json()

r2 = requests.get(url = URL, params = PROMQL2)
cpu = r2.json()

# Assign results object to results
results = r1.json()['data']['result']

# Build a list of all labelnames used.
labelnames = set()
for result in results:
      labelnames.update(result['metric'].keys())

# Canonicalize
#labelnames.discard('__name__')
#labelnames = sorted(labelnames)

writer = csv.writer(sys.stdout)

# Write the header,
writer.writerow(['name', 'timestamp', 'value'] + labelnames)

# Write the samples.
for result in results:
    l = [result['metric'].get('__name__', '')] + result['value']
    for label in labelnames:
        l.append(result['metric'].get(label, ''))
    writer.writerow(l)
