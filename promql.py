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

r2 = requests.get(url = URL, params = PROMQL2)

r1_json = r1.json()['data']['result']
r2_json = r2.json()['data']['result']

# Build a list of all labelnames used.
labelnames = set()
for result in r1_json:
      labelnames.update(result['metric'].keys())

# Canonicalize
labelnames.discard('__name__')
labelnames = sorted(labelnames)

writer = csv.writer(sys.stdout)

# Write the header,
writer.writerow(['query', 'timestamp', 'value'] + labelnames)

# Write the samples.
for result in r1_json:
    l1 = ['memory'] + result['value']
    for label in labelnames:
        l1.append(result['metric'].get(label, ''))
    writer.writerow(l1)


# Build a list of all labelnames used.
labelnames = set()
for result in r2_json:
      labelnames.update(result['metric'].keys())

# Canonicalize
labelnames.discard('__name__')
labelnames = sorted(labelnames)

writer = csv.writer(sys.stdout)

# Write the header,
writer.writerow(['query', 'timestamp', 'value'] + labelnames + ['job'])

# Write the samples.
for result in r2_json:
    l2 = ['cpu'] + result['value']
    for label in labelnames:
        l2.append(result['metric'].get(label, ''))
    l2.append('node')
    writer.writerow(l2)
