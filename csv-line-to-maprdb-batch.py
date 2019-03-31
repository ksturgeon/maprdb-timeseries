from mapr.ojai.storage.ConnectionFactory import ConnectionFactory
import time
import os
import json
import sys
import csv
import getpass
from datetime import datetime 

print("Non-secure cluster only.\n")
host = raw_input("DAG host:")
username = raw_input("username [mapr]:")
if len(username) == 0:
  username="mapr"
password = getpass.getpass(prompt = "Password [maprmapr]:")
if len(password) == 0:
  password="maprmapr"
tbl_path = raw_input("Table path [/demo-tables/timeseries]:")
if len(tbl_path) == 0:
  tbl_path="/demo-tables/timeseries"
source_file = raw_input("Input File [10Simoutput.csv]:")
if len(source_file) == 0:
  source_file="10Simoutput.csv"


#Create a connection to data access server
connection_str = "{}:5678?auth=basic;user={};password={};ssl=false".format(host,username,password) 
connection = ConnectionFactory.get_connection(connection_str=connection_str)

# Get a store and assign it as a DocumentStore object
if connection.is_store_exists(store_path=tbl_path):
    document_store = connection.get_store(store_path=tbl_path)
else:
    document_store = connection.create_store(store_path=tbl_path)


i=0
x=0
document_list = []

#Open the file
with open(source_file) as f:
  reader = csv.DictReader(f, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
  
  t = time.time()
  for row in reader:

    i=i+1
    #change the friendly AM/PM to 24hr
    format = '%Y-%m-%d %I:%M:%S %p'

    #modify the Date string to a unix epoch
    row['Date'] = datetime.strptime(row['Date'], format).strftime('%s')    

    d = dict(row)
    d['_id'] = row['Date']

    #Batch documents ten at a time
    if x<10:
      document_list.append(d)
      x=x+1
    else:
      #Write document
      document_store.insert_or_replace(doc_stream=document_list)
      x=0
      document_list = []  

    t = time.time() - t
    sys.stdout.write("\r %4.1f docs per second" % (1/t))
    sys.stdout.flush()    

  print('\n{} documents written'.format(i))

connection.close()  
