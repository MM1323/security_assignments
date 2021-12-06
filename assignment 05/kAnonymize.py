import pandas as pd
import numpy as np
from io import StringIO
import os
import sys



def main():
    data = "placeholder"
    k = 3 # place holder
    if (len(sys.argv) == 3):
        k = int(sys.argv[2])
        data = pd.read_csv(sys.argv[1])
    else:
        data = pd.read_csv('CensusDataMini.csv')
    
    print(k)
    # Drops the first column
    #data.drop(data.columns[[0]], axis=1, inplace=True)
    finalData = parseData(data, k)
    saveData(finalData)
    print("Hello")
    print(finalData)
    print("TestK", TestK(finalData, k))


    # if isK == False:
    #     reduceAge(data)
    # isK = parseData(data, k)
    # # if isK == False:
    # #     reduceHours(data)
    # # isK = parseData(data, k)
    # print(isK)

    # while not isK:    
        
    # saveData(data)
    # reduceAge(data)
    # reduceHours(data)
    # print(data)
    # saveData(data)


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
    group = data.groupby(['Occupation', 'Age','Race', 'Sex', 'HoursPerWeek'])
    # groupsSize = group.reset_index()
    # testing = data.groupby(["Name", "City"]).size().to_frame(name='count').reset_index()


    #testing = pd.DataFrame(group.size().reset_index(name='Group_Count'))
    data2 = pd.DataFrame()
    dataFinal = pd.DataFrame()

    for item in group.groups.keys():
        if (group.get_group(item).shape[0] < k):
            data2 = data2.append(group.get_group(item), ignore_index= True)
        else:
            dataFinal = dataFinal.append(group.get_group(item), ignore_index= True)


    changeCounter = 0        

    for i in range(0, data2.shape[0], k):
        subGroup = data2.iloc[i:i+k]
        ChangeCategoryValue('Occupation', subGroup, changeCounter)
        ChangeCategoryValue('Age', subGroup, changeCounter)
        ChangeCategoryValue('Race', subGroup, changeCounter)
        ChangeCategoryValue('Sex', subGroup, changeCounter)
        ChangeCategoryValue('HoursPerWeek', subGroup, changeCounter)
    if(data2.shape[0]%k>0):
        subGroup = data2.iloc[data2.shape[0]-(data2.shape[0]%k):data2.shape[0]]
        temp = data2.iloc[data2.shape[0]-(data2.shape[0]%k)-1]
        subGroup['Occupation'] = temp['Occupation']
        subGroup['Age'] = temp['Age']
        subGroup['Race'] = temp['Race']
        subGroup['Sex'] = temp['Sex']
        subGroup['HoursPerWeek'] = temp['HoursPerWeek']
        changeCounter = changeCounter + data2.shape[0]-(data2.shape[0]%k)*5


    #groupFinal = data2.groupby(['Age', 'Occupation', 'Race', 'Sex', 'HoursPerWeek'])
    #testingFinal = pd.DataFrame(groupFinal.size().reset_index(name="Group_Count"))
    for Group_Count, item in data2.iterrows():
        dataFinal = dataFinal.append(item, ignore_index= True)    
    #print(dataFinal)
    print("Reduced precision of " + str(changeCounter) + " attributes")
    return dataFinal

    # for x, y in testing.iterrows():
    #     print("____")
    #     print(x)
    #     print()
    #     print(y)
    #     print("____")


    # print(type(group))
    # print(groupsSize.tolist())
    # print(group.size())
    # size = group.size()
    # test = group.first()
    # test = group.get_group('Age')
    # print(group.groups)
    # print(group.keys)
    # for key in group:
    #     print("key: ", key)
    #     for value in key:
    #         print(value)


    # print(group.size())
    # for x in size:
    #     # print(x)
    #     if x < k:            
    #         return False
    
    
    
def ChangeCategoryValue(category, subgroup, changeCounter):
    val = subgroup[category]
    if (val.nunique()>1):
        subgroup[category] = subgroup[category].mode()[0]
    return changeCounter+1


def TestK(dataFinal, k):
    return (min(list(dataFinal.groupby(['Occupation', 'Age', 'Race', 'Sex', 'HoursPerWeek']).size())) >= k)


"""
def reduceAge(data):
    # print("Hi")
    # data.loc[(data.age >= 12), ['section']] = 'M'
    data.loc[(data.Age >= 1) & (data.Age <= 19), ['Age']] = 20
    data.loc[(data.Age >= 20) & (data.Age <= 29), ['Age']] = 30
    data.loc[(data.Age >= 30) & (data.Age <= 39), ['Age']] = 40
    data.loc[(data.Age >= 40) & (data.Age <= 49), ['Age']] = 50
    data.loc[(data.Age >= 40) & (data.Age <= 49), ['Age']] = 50
    data.loc[(data.Age >= 50) & (data.Age <= 59), ['Age']] = 60
    data.loc[(data.Age >= 60) & (data.Age <= 69), ['Age']] = 70
    data.loc[(data.Age >= 70) & (data.Age <= 79), ['Age']] = 80
    data.loc[(data.Age >= 80), ['Age']] = 90
    print(data)



def reduceHours(data):
    data.loc[(data.HoursPerWeek >= 0) & (data.HoursPerWeek <=7), ['HoursPerWeek']] = 8
    data.loc[(data.HoursPerWeek >= 8) & (data.HoursPerWeek <=15), ['HoursPerWeek']] = 16
    data.loc[(data.HoursPerWeek >= 16) & (data.HoursPerWeek <=23), ['HoursPerWeek']] = 24
    data.loc[(data.HoursPerWeek >= 24) & (data.HoursPerWeek <=31), ['HoursPerWeek']] = 32
    data.loc[(data.HoursPerWeek >= 32) & (data.HoursPerWeek <=39), ['HoursPerWeek']] = 40
    data.loc[(data.HoursPerWeek >= 40) & (data.HoursPerWeek <=47), ['HoursPerWeek']] = 48
    data.loc[(data.HoursPerWeek >= 48) & (data.HoursPerWeek <=55), ['HoursPerWeek']] = 56
    data.loc[(data.HoursPerWeek >= 56) & (data.HoursPerWeek <=63), ['HoursPerWeek']] = 64
    data.loc[(data.HoursPerWeek >= 64) & (data.HoursPerWeek <=71), ['HoursPerWeek']] = 72
    data.loc[(data.HoursPerWeek >= 72) & (data.HoursPerWeek <=79), ['HoursPerWeek']] = 80
    data.loc[(data.HoursPerWeek >= 80), ['HoursPerWeek']] = 88
    print(data)
"""

def saveData(data):
    data.to_csv("kCensusData.csv", index=False, encoding='utf8')

if __name__ == "__main__":
    main()

# Rounding the age 
# 2 - rounding the age to the nearest 10 if it (round up) & hours worked per week round up to nearest 10 (up)
# 3 - Rounding to the nearest 5 (up) && HWPW round up to 5 && race take out every thing after hiphan == problem with armeed forces (do an expection to take away all races and keep the rest)
# 4 - rounding the age to the nearest 10 && HWPW round up to 10
# 5 - rounding the age to the nearest 10 && HWPW round up to 10 && take out race
# 6 - rounding the age to the nearest 10 && HWPW round up to 10 && take out race && take out gender



