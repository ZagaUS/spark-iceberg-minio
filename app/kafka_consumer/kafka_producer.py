from confluent_kafka import Producer
import json
import yaml

p = Producer({'bootstrap.servers': 'localhost:19092'})

with open('../trace.json') as f:
    for line in f:
        d = yaml.safe_load(line)
        jd = json.dumps(d)
        p.produce('observai_main_traces_1', jd)
        p.flush()

