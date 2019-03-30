import time
import os
import json
import sys
import csv

#Open the file
with open("10Simoutput.csv") as f:
  reader = csv.DictReader(f)
  outputfile = open("10Simoutput.json", "w+")
  for row in reader:
    
    print(json.dumps(dict(row)))
    outputfile.write(json.dumps(sorted(dict(row))))
  outputfile.close()
