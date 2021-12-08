import pandas as pd
import numpy as np
from io import StringIO
import os
import sys


def main():
    print("Hello")

    data = "placeholder"
    l = 3 # place holder
    if (len(sys.argv) == 3):
        l = int(sys.argv[2])
        data = pd.read_csv(sys.argv[1])
    else:
        data = pd.read_csv('kCensusData.csv')
    
    getData(data, l)


def getData(data, l):
    group = data.groupby(['Occupation', 'Age', 'Race', 'Sex', 'HoursPerWeek'])

    tempData = pd.DataFrame()
    dataFinal = pd.DataFrame()

    # Iterate through the groups and if l diverse, add to final || if not, add to data that needs to be changed
    for item in group.groups.keys():
        oneGroup = group.get_group(item)
        numberofUnique = len(pd.unique(oneGroup['EducationNum']))
        
        if (numberofUnique < l):
            tempData = tempData.append(group.get_group(item), ignore_index=True)
        else:
            dataFinal = dataFinal = dataFinal.append(group.get_group(item), ignore_index= True)
        # break

    changeCounter = 0

    #start combining groups
    # for each of the uncommon groups

    while True:
        
        



    

def TestI():
    print("Hi")





def saveData(data):
    data.to_csv("lCensusData.csv", index=False, encoding='utf8')

if __name__ == "__main__":
    main()
