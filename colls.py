import os, csv, json

inputfile = os.path.abspath("data/all-colls.csv")
outputfile = ("api/collections/index.json")
os.makedirs(os.path.dirname(outputfile), exist_ok=True)
# print(inputfile)
# print(outputfile)

# # Read the CSV and add data to a dictionary
with open(inputfile) as csvFile:
  csvReader = csv.DictReader(csvFile)
  # for csvRow in csvReader:
  #   data[csvRow] = {[csvRow]}
  #   fullname = csvRow["fullname"]
  #   data[fullname] = csvRow
# print(data)

  # Add data to a root node
  root = {}
  root["collections"] = [row for row in csvReader]
  # # Write data to JSON file
  with open(outputfile, "w") as jsonFile:
    # jsonFile.write(json.dumps([row for row in csvReader], indent=4))
    jsonFile.write(json.dumps(root, indent=4))
  print("Created JSON file for collections")


# Simplified process adaptaed from the one found on https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json (question)
# csvFile = open(inputfile, 'r')
# outFile = open(outputfile, 'w')
# reader = csv.DictReader(csvFile)
# out = json.dumps([row for row in reader], indent=4)
# outFile.write(out)