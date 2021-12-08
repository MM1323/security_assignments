import pandas as pd
import numpy as np
from io import StringIO
import os
import sys
import warnings
warnings.filterwarnings('ignore')


def main():
    data = "placeholder"
    k = 3 # place holder
    if (len(sys.argv) == 3):
        k = int(sys.argv[2])
        data = pd.read_csv(sys.argv[1])
    else:
        # If no command line arguement is passed
        data = pd.read_csv('CensusData.csv')
    
    # Drops the first column
    # data.drop(data.columns[[0]], axis=1, inplace=True)

    # Parse the data
    finalData = parseData(data, k)

    # Save the data
    saveData(finalData)

    # Testing
    # print("Hello")
    # print(finalData)
    # print("TestK", TestK(finalData, k))


"""
Create two new data frames, one to work in and the other for the final results
Move rows less than k to new work data frame
Move rows more than k to final results data frame
get random rows in the new data frame
find which columns are different
repeat until k is reached

once merged, add back into initial data frame

"""
def parseData(data, k):
    # Group them
    group = data.groupby(['Occupation', 'Age','Race', 'Sex', 'HoursPerWeek'])
    
    # Two temp Frames
    data2 = pd.DataFrame()
    dataFinal = pd.DataFrame()

    # Iterate through each group
    for item in group.groups.keys():
        if (group.get_group(item).shape[0] < k):
            data2 = data2.append(group.get_group(item), ignore_index= True)
        else:
            dataFinal = dataFinal.append(group.get_group(item), ignore_index= True)

    changeCounter = 0
    
    # Change each category
    for i in range(0, data2.shape[0], k):
        subGroup = data2.iloc[i:i+k]
        ChangeCategoryValue('Occupation', subGroup, changeCounter)
        ChangeCategoryValue('Age', subGroup, changeCounter)
        ChangeCategoryValue('Race', subGroup, changeCounter)
        ChangeCategoryValue('Sex', subGroup, changeCounter)
        ChangeCategoryValue('HoursPerWeek', subGroup, changeCounter)

    # Hard Code the changes
    if(data2.shape[0]%k>0):
        subGroup = data2.iloc[data2.shape[0]-(data2.shape[0]%k):data2.shape[0]]
        temp = data2.iloc[data2.shape[0]-(data2.shape[0]%k)-1]
        subGroup['Occupation'] = temp['Occupation']
        subGroup['Age'] = temp['Age']
        subGroup['Race'] = temp['Race']
        subGroup['Sex'] = temp['Sex']
        subGroup['HoursPerWeek'] = temp['HoursPerWeek']
        changeCounter += data2.shape[0]-(data2.shape[0]%k)*5

    # Add to the final group
    for Group_Count, item in data2.iterrows():
        dataFinal = dataFinal.append(item, ignore_index= True)    

    # Return the date and print precision
    print("Reduced precision of " + str(changeCounter) + " attributes")
    return dataFinal

    
def ChangeCategoryValue(category, subgroup, changeCounter):
    val = subgroup[category]
    if (val.nunique()>1):
        subgroup[category] = subgroup[category].mode()[0]
    return changeCounter+1


""" Test if k anonymized"""
def TestK(dataFinal, k):
    return (min(list(dataFinal.groupby(['Occupation', 'Age', 'Race', 'Sex', 'HoursPerWeek']).size())) >= k)


""" Save the data given"""
def saveData(data):
    data.to_csv("kCensusData.csv", index=False, encoding='utf8')


""" Call on main"""
if __name__ == "__main__":
    main()