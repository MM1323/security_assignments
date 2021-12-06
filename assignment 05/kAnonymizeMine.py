import pandas as pd
import numpy as np
from io import StringIO
import os



def main():
    # data = pd.read_csv('CensusDataMini.csv')
    data = pd.read_csv('CensusData.csv')
    k = 3 # place holder

    # print(data)

    # df.columns is zero-based pd.Index
    # df = df.drop(df.columns[[0, 1, 3]], axis=1)

    # Drops the first column
    data.drop(data.columns[[0]], axis=1, inplace=True)
    # print(data)

    isK = False

    isK = parseData(data, k)
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

    
def reGroup(data, group, testing, k, iterations):

    for x in range(len(testing)):
        group_count = testing.iloc[[0], [5]].values.tolist()[0][0]
        # print(x)
        # print(group_count)

        if (group_count < k):
            print("We have to adjust")
            
            reduceAge(data)
            reduceHours(data)

            maxReduceAge(data)
            maxReduceHours(data)
            deleteHours(data)
            # if (iterations == 0):
            #     reduceAge(data)
            # elif(iterations):
            #     reduceHours(data)


        break
    # return True
    return False




def parseData(data, k):
    group = data.groupby(['Occupation', 'Race', 'Sex', 'Age', 'HoursPerWeek'])
    # groupsSize = group.reset_index()
    # testing = data.groupby(["Name", "City"]).size().to_frame(name='count').reset_index()
    testing = pd.DataFrame(group.size().reset_index(name="Group_Count"))

    iterations = 0
    isDone = True
    while isDone:
        isDone = reGroup(data, group, testing, k, iterations)
        group = data.groupby(['Occupation', 'Race', 'Sex', 'Age', 'HoursPerWeek'])
        testing = pd.DataFrame(group.size().reset_index(name="Group_Count"))
        iterations += 1

    # print(group)
    # print(testing)
    print("___________")
    print(testing.iloc[0], "\n")
    print(testing.iloc[1], "\n")
    print(testing.iloc[2], "\n")
    print(testing.iloc[3], "\n")
    print(testing.iloc[4], "\n")
    print(testing.iloc[5], "\n")
    print(testing.iloc[6], "\n")
    print("___________")

    # saveData(data)

    # group_count = testing.iloc[[0], [5]].values.tolist()[0][0]
    
    # print(testing.iloc[[2] , [5]], "\n")

    # # testing.iloc[[0], [5]] = 100
    


    
    # print(testing.iloc[3])
    # placeOne = 0
    # placeTwo = 1

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
    return True
    
    
def deleteHours(data):
    # data.loc[(data.Race == "Amer-Indian-Eskimo"), ['HoursPerWeek']] = "*"
    data.loc[data['Race'] == "Amer-Indian-Eskimo", 'HoursPerWeek'] = "*"
    # print(data)



def reduceAge(data):
    data.loc[(data.Age >= 1) & (data.Age <= 19), ['Age']] = 20
    data.loc[(data.Age >= 21) & (data.Age <= 29), ['Age']] = 30
    data.loc[(data.Age >= 31) & (data.Age <= 39), ['Age']] = 40
    data.loc[(data.Age >= 41) & (data.Age <= 49), ['Age']] = 50
    data.loc[(data.Age >= 51) & (data.Age <= 59), ['Age']] = 60
    data.loc[(data.Age >= 61) & (data.Age <= 69), ['Age']] = 70
    data.loc[(data.Age >= 71) & (data.Age <= 79), ['Age']] = 80
    data.loc[(data.Age >= 81), ['Age']] = 90
    # print(data)


def maxReduceAge(data):
    # 30 -- 50 -- 70 -- 90
    # 20 -- 40 -- 60 -- 80
    data.loc[(data.Age == 20), ['Age']] = 30
    data.loc[(data.Age == 40), ['Age']] = 50
    data.loc[(data.Age == 60), ['Age']] = 70
    data.loc[(data.Age == 80), ['Age']] = 90

   
def maxReduceHours(data):
    # 30 -- 50 -- 70 -- 90
    # 20 -- 40 -- 60 -- 80
    data.loc[(data.HoursPerWeek == 20), ['HoursPerWeek']] = 30
    data.loc[(data.HoursPerWeek == 40), ['HoursPerWeek']] = 50
    data.loc[(data.HoursPerWeek == 60), ['HoursPerWeek']] = 70
    data.loc[(data.HoursPerWeek == 80), ['HoursPerWeek']] = 90


def reduceHours(data):
    data.loc[(data.HoursPerWeek >= 1) & (data.HoursPerWeek <= 19), ['HoursPerWeek']] = 20
    data.loc[(data.HoursPerWeek >= 21) & (data.HoursPerWeek <= 29), ['HoursPerWeek']] = 30
    data.loc[(data.HoursPerWeek >= 31) & (data.HoursPerWeek <= 39), ['HoursPerWeek']] = 40
    data.loc[(data.HoursPerWeek >= 41) & (data.HoursPerWeek <= 49), ['HoursPerWeek']] = 50
    data.loc[(data.HoursPerWeek >= 51) & (data.HoursPerWeek <= 59), ['HoursPerWeek']] = 60
    data.loc[(data.HoursPerWeek >= 61) & (data.HoursPerWeek <= 69), ['HoursPerWeek']] = 70
    data.loc[(data.HoursPerWeek >= 71) & (data.HoursPerWeek <= 79), ['HoursPerWeek']] = 80
    data.loc[(data.HoursPerWeek >= 81), ['HoursPerWeek']] = 90
    # print(data)


def saveData(data):
    data.to_csv("kCensusData.csv", index=False, encoding='utf8')

def checkK():
    print("Hi")


main()

# Rounding the age 
# 2 - rounding the age to the nearest 10 if it (round up) & hours worked per week round up to nearest 10 (up)
# 3 - Rounding to the nearest 5 (up) && HWPW round up to 5 && race take out every thing after hiphan == problem with armeed forces (do an expection to take away all races and keep the rest)
# 4 - rounding the age to the nearest 10 && HWPW round up to 10
# 5 - rounding the age to the nearest 10 && HWPW round up to 10 && take out race
# 6 - rounding the age to the nearest 10 && HWPW round up to 10 && take out race && take out gender



