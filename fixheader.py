import shutil

with open("Simoutput.csv") as from_file:
  line = from_file.readline()
  line = line.replace(".","")

  with open("ASimoutput.csv",mode="w") as to_file:
    to_file.write(line)
    shutil.copyfileobj(from_file, to_file)

  
