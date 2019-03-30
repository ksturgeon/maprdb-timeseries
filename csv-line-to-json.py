import time
import os
import json
import sys
import csv

#Open the file
with open("10Simoutput.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(json.dumps(dict(row)))

    time.sleep(3)

