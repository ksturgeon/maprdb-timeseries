import time
import os
import json
import sys
import csv
from datetime import datetime 

i=1

#Open the file
with open("10Simoutput.csv") as f:
  reader = csv.DictReader(f, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
  with open("10Simoutput.json", "w+") as ofile:
    t = time.time()
    for row in reader:

      #change the friendly AM/PM to 24hr
      format = '%Y-%m-%d %I:%M:%S %p'

      #modify the Date string to a unix epoch
      row['Date'] = datetime.strptime(row['Date'], format).strftime('%s')    
      #print(row['Date'])

      d=dict(row)
      d['_id']=row['Date']
      #print(json.dumps(dict(row)))
      ofile.write(json.dumps(d))
      
      #time.sleep(1) 
      i=i+1

  print('\n{} documents written'.format(i))  
