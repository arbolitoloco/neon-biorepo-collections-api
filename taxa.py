import os, csv, json

inputfile = os.path.abspath("data/all-colls.csv")
outputfile = ("api/taxa/index.json")
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
# print(inputfile)
# print(outputfile)

# Read the CSV and add data to a dictionary
data = {}
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    taxon = csvRow["taxon"]
    data[taxon] = csvRow
print(data)

# Add data to a root node
root = {}
root["taxa"] = data

# Write data to JSON file
with open(outputfile, "w") as jsonFile:
  jsonFile.write(json.dumps(root, indent=4))
print("Created JSON file for taxa")