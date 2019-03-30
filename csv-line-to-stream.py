from confluent_kafka import Producer
import time, datetime
import os
import json
import sys
import csv

#Set up my producer 
p = Producer({'streams.producer.default.stream': '/demo/demostream'})

#Open the file
with open("10Simoutput.csv") as f:
  reader = csv.DictReader(f)
  outputfile = open("10Simoutput.json", "w+")
  for row in reader:
    #write to the producer
    print('\n Writing Record at: ' + str(datetime.datetime.now()))
    p.produce('topic1', json.dumps(dict(row)))
    p.flush()

    #print(json.dumps(dict(row)))

    #write to a file because we can
    outputfile.write(json.dumps(dict(row)))

    #Sleep if we want to
    #time.sleep(1)

  outputfile.close()
