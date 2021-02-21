#  imports
import csv
import pandas as pd

# file names
file1 = 'bright_stars.csv'
file2 = 'brown_dwarf.csv'

# creating empty lists and saving data from files into lists
data1 = []
data2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        data1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data2.append(i)

# getting headers
header1 = data1[0]
header2 = data2[0]

# getting planet data
planet_data1 = data1[1:]
planet_data2 = data2[1:]

# merging headers
header = header1+header2

# creating empty list and merging planet data in it
planet_data =[]

# writing data in csv file
for i in planet_data1:
    planet_data.append(i)
for j in planet_data2:
    planet_data.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)   
    csvwriter.writerows(planet_data)
    