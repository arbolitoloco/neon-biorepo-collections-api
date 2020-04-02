import os, csv, json, numpy as np
filename = "all-colls.csv"

# Read inputfile
def getsSubdirectories(inputfile, colstart, colend):
  inputpath = os.path.abspath("data/"+inputfile)
  with open(inputpath, encoding="utf-8-sig") as csvFile:
    csvReader = csv.reader(csvFile)
    for csvRow in csvReader:
      subdirsArr = []
      # Gets first cols and pass them to subdirs separated by "/"
      for csvCol in range(colstart, colend):
        # print(csvRow[csvCol])
        subdirsArr.append(csvRow[csvCol].rstrip())
      # print("end of line")
      # print(subdirsArr)
      subdirsPath = "/".join(subdirsArr)
      outputpath = os.path.abspath("api/"+subdirsPath)
      print(outputpath)

# Next steps: 1. make directories using outputpaths extracted from file (keep only unique, remove first entry because it's the header) ; 2. create separate files for each valid path    

# def exportsToJson(inputfile):
#   # Create JSON file with root and starting at col 3
#   inputpath = os.path.abspath("data/"+inputfile)
#   data = {}
#   with open(inputpath, encoding="utf-8-sig") as csvFile:
#     csvReader = csv.DictReader(csvFile)
#     for csvRow in csvReader:
#       print(csvRow)

  # # Write data to JSON file
  # with open(outputfile, "w") as jsonFile:
  #   jsonFile.write(json.dumps(root, indent=4))
  # print("Attempted to create JSON file")

getsSubdirectories(filename, 0, 2)
# exportsToJson(filename)