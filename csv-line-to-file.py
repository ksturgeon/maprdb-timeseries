import time
import os
import json
import sys
import csv
from datetime import datetime 

i=1

#Open the file
with open("10Simoutput.csv") as f:
  reader = csv.DictReader(f)
  with open("10Simoutput.json", "w+") as ofile:
    t = time.time()
    for row in reader:

      #change the friendly AM/PM to 24hr
      format = '%Y-%m-%d %I:%M:%S %p'

      #modify the Date string to a unix epoch
      row['Date'] = datetime.strptime(row['Date'], format).strftime('%s')    
      #print(row['Date'])

      #print(json.dumps(dict(row)))
      ofile.write(json.dumps(dict(row)))
      
      #time.sleep(1) 
      i=i+1
      t = time.time() - t
      print("%4.1f doc per second" % (1 /t), end='\r')

  print('\n{} documents written'.format(i))  
