import pandas as pd
import numpy as np
from io import StringIO
import os
import sys
import warnings
warnings.filterwarnings('ignore')


def main():
    data = "placeholder"
    l = 3 # place holder
    if (len(sys.argv) == 3):
        l = int(sys.argv[2])
        data = pd.read_csv(sys.argv[1])
    else:
        # If no command line arguement is passed
        data = pd.read_csv('kCensusData.csv')

    # Make if diverse
    dataFinal = Diversify(data, l)

    # Save the data
    saveData(dataFinal)

""" 
Group the data
If its l diverse, do change anything
If its not l diverse, group the values to make it so 
"""
def Diversify(data, l):
    group = data.groupby(['Occupation', 'Age','Race', 'Sex', 'HoursPerWeek'])
    data2 = pd.DataFrame()
    dataFinal = pd.DataFrame()

    # Iterate through the groups
    for item in group.groups.keys():
        k = group.get_group(item).shape[0]
        if ((len(pd.unique(group.get_group(item)['EducationNum']))) < l):
            data2 = data2.append(group.get_group(item), ignore_index= True)
        else:
            dataFinal = dataFinal.append(group.get_group(item), ignore_index= True)


    x = 0
    y= 0
    changeCounter = 0        

    # Iterate and change
    while ((k + x + y) < data2.shape[0]):
        subGroup = data2.iloc[x:k+x+y]
        changeCounter = ChangeCategoryValue('Occupation', subGroup, changeCounter)
        changeCounter = ChangeCategoryValue('Age', subGroup, changeCounter)
        changeCounter = ChangeCategoryValue('Race', subGroup, changeCounter)
        changeCounter = ChangeCategoryValue('Sex', subGroup, changeCounter)
        changeCounter = ChangeCategoryValue('HoursPerWeek', subGroup, changeCounter)
        if (len(pd.unique(subGroup['EducationNum'])) >= l):
            x = k + x + y
            y = 0
        else:
            y= y + 1

    # Hard code last few line
    subGroup = data2.iloc[x:data2.shape[0]]
    if(len(pd.unique(subGroup['EducationNum'])) < l):
        temp = data2.iloc[-3:]
        subGroup['Occupation'] = temp['Occupation'].iloc[0]
        subGroup['Age'] = temp['Age'].iloc[0]
        subGroup['Race'] = temp['Race'].iloc[0]
        subGroup['Sex'] = temp['Sex'].iloc[0]
        subGroup['HoursPerWeek'] = temp['HoursPerWeek'].iloc[0]
        changeCounter += (data2.shape[0]-x)*5

    # Add to final return group
    for Group_Count, item in data2.iterrows():
        dataFinal = dataFinal.append(item, ignore_index= True)    

    # Print and return data
    print("Reduced precision of " + str(changeCounter) + " attributes")
    return dataFinal

""" Change the category value"""
def ChangeCategoryValue(category, subgroup, changeCounter):
    val = subgroup[category]
    if (val.nunique()>1):
        subgroup[category] = subgroup[category].mode()[0]
    return changeCounter+1

""" Save the data given"""
def saveData(data):
    data.to_csv("lCensusData.csv", index=False, encoding='utf8')

""" Call on main"""
if __name__ == "__main__":
    main()