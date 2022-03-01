import csv
with open('grades.csv', newline='') as csvfile:
    reader = csv.reader(csvfile )
    for row in reader:
        # print(row['name: '], row['Math: '], row['Physics: '], row['differenciel: '], row['Programming: '], row['Circuit: '], row['Art: '])
        print('Name: %s,\n' 'Math: %s,\n' 'Physics: %s, \n' 'Differenciel: %s, \n' 'Programming: %s, \n' 'Circuit: %s, \n' 'Art: %s, \n'%(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
