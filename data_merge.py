# imports 
import csv
import pandas as pd

# getting brown dwarfs data
df = pd.read_csv("brown_dwarf.csv")

# deleting na values
df = df[df["distance"].notna()]
df = df[df["mass"].notna()]
df = df[df["radius"].notna()]

# changing masses , radiuses to float and converting to solar mass , solar radius
mass_list = []
radius_list = []
for i in df["mass"]:
    i = float(i)
    i = i*0.000954588
    mass_list.append(i)
for i in df["radius"]:
    i = float(i)
    i = i*0.102763
    radius_list.append(i)
df.mass = mass_list
df.radius = radius_list

# creating csv file
df.to_csv("brown_dwarfs_modified.csv",index=False)



# file names
file1 = 'bright_stars.csv'
file2 = 'brown_dwarfs_modified.csv'

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
for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

# writing data in csv file
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)   
    csvwriter.writerows(planet_data)

