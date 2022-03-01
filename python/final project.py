import csv
csvFile = open ( example.csv )
csvReader = csv.reader (csvFile)
csvData = list ( csvReader )
