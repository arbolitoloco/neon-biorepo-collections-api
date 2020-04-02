import os, csv, json

inputfile = os.path.abspath("data/all-colls.csv")
outputfile = ("api/collections/all.json")
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
# print(inputfile)
# print(outputfile)

# Read the CSV and add data to a dictionary
data = {}
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    fullname = csvRow["fullname"]
    data[fullname] = csvRow
print(data)

# Add data to a root node
root = {}
root["collections"] = data

# Write data to JSON file
with open(outputfile, "w") as jsonFile:
  jsonFile.write(json.dumps(root, indent=4))
print("Created JSON file for collections")