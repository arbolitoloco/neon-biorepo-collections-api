import os, csv, json

inputfile = os.path.abspath("data/categories.csv")
outputfile = os.path.abspath("api/categories/all.json")
print(inputfile)
print(outputfile)

# Read the CSV and add data to a dictionary
data = {}
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    shortname = csvRow["shortname"]
    data[shortname] = csvRow
print(data)

# Add data to a root node
root = {}
root["categories"] = data

# Write data to JSON file
with open(outputfile, "w") as jsonFile:
  jsonFile.write(json.dumps(root, indent=4))
print("Attempted to create JSON file")