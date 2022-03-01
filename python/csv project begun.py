from itertools import count
from math import *
import csv
# For the average
from statistics import mean
from tkinter.font import names

from numpy import average 


with open("csv start.csv") as csvfile:
    reader = csv.reader(csvfile )
    names = []
    tool = []
    numbers = []
    for name in reader:
        names.append(name[0])
        numbers.append(name[1:])
    majmoe = []
    jam = 0
    for num in numbers:
        tul = len(num)
        tool.append(tul)
        for adad in num:
            adad = int(adad)
            jam += adad
        
        majmoe.append(jam)
        jam = 0
    #print(majmoe)
    #print(tool)
    lest = []
    moadel = []
    tedad = len(names)
    martabe = 0
    while martabe < tedad:
        for jam in majmoe:
            natije = majmoe[martabe]/tool[martabe]
        moadel.append(natije)
            #print(names[martabe], moadel[martabe])
        martabe += 1

        lest.append(names)
        lest.append(moadel)

#def calculate_averages(input_file_name, output_file_name):
    #moadel = []
    #tedad = len(names)
    #artabe = 0
    #while martabe < tedad:
        #for jam in majmoe:
            #natije = majmoe[martabe]/tool[martabe]
        #moadel.append(natije)
        #print(names[martabe], moadel[martabe])
        #martabe += 1

    #lest.append(names)
    #lest.append(moadel)
    
#calculate_averages(name, average)
moadel.sort()
for item in moadel:
    moadel.find(item)


#def calculate_sorted_averages(input_file_name, output_file_name):
    #for name in names:
        #print(name, )#reverse sorted average)


#def calculate_three_best(input_file_name, output_file_name):
    #for name in names:
        #print(name, )#top three)


#def calculate_three_worst(input_file_name, output_file_name):
    


#def calculate_average_of_averages(input_file_name, output_file_name):
    