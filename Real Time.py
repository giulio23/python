from datetime import datetime
import requests
import json
import random
import time

class Machine:
    def __init__(self, output_rate, output_variance):
        self.output_rate = output_rate
        self.output_variance = output_variance
    
    def produce(self):
        actual_rate = self.output_rate + random.randrange(-self.output_variance, self.output_variance)
        time.sleep(3600 / actual_rate)  # Amount of time for one output
        return 1

def report_pbit(time_elapsed, batch_sz):
    rate = batch_sz / time_elapsed * 3600
    url = "paste here the Push URL"

    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")
    data = [{'rate': rate, 'date': now}]
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=data)
    return rate

m = Machine(2000, 95)
inventory = []
batch = []
batch_sz = 1
start = time.time()

while True:
    out = m.produce()
    batch.append(out)

    if len(batch) == batch_sz:
        elapsed_time = time.time() - start
        rate = report_pbit(elapsed_time, batch_sz)
        start = time.time()
        batch = []
        print(f"Batch done with rate {rate}")

    # Add a condition to break the loop if necessary
    # if some_condition:
    #     break
