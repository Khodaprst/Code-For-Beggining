import csv
from statistics import mean

with open('grades.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #print (row)
        name = row[0]
        these = list()
        # the lis wil containt from of grades
        for grade in row[1:]: #because the first one is the name
            these.append(int(grade))
            #print(name, grade, these)
        
        print('average of %s is %2.2f' %(name, mean(these)))