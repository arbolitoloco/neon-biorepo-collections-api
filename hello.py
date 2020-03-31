import os, csv, json
# import pandas as pd

inputfile = os.path.abspath("data/categories.csv")
outputfile = os.path.abspath("api/categories/all.json")

# df = pd.read_csv (inputpath)
# df.to_json (outputpath, orient='table')

# Read the CSV and add data to a dictionary
data = {}
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    shortname = csvRow["shortname"]
    data[shortname] = csvRow
# print(data)

# Add data to a root node
root = {}
root["categories"] = data

# Write data to JSON file
with open(outputfile, "w") as jsonFile:
  jsonFile.write(json.dumps(root, indent=4))