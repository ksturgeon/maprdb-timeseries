# maprdb-timeseries
- Step 1 - add your production csv data
- Step 2 - run "fixheader.py" to strip "." char out of column headings
- Step 3 - run cluster-setup.sh
- Optional - edit cluster-setup.sh to create a table named /demo-tables/timeseries2 so the queries can work.

**option 1** - Create json file and load to mapr-db
- Step 1 - run "csv-line-to-json.py"
- Step 2 - copy json file to the cluster "hadoop fs -copyFromLocal /<filename>.json /demo-files/"
- Step 3 - load the data - "mapr importJSON -src /demo-files/<filename>.json -dst /demo-tables/timeseries -mapreduce false"

**option 2** - use the Data Access Gateway python library (slower but more control over document format and fields)
- Step 1 - run "csv-line-to-maprdb-batch.py" - fill in the prompts
