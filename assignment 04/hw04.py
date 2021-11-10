import json
import matplotlib.pyplot as plt
from numpy import random



def createPlot(websites, values):

    # Actual plot creation
    plt.style.use('ggplot')

    x_pos = [i for i, _ in enumerate(websites)]
    plt.bar(x_pos, values, color='green')

    plt.xlabel("Domain")
    plt.ylabel("Number of Cookies")
    plt.title("First Party Cookies")

    plt.xticks(x_pos, websites)

    plt.savefig('test.png')
    plt.show()
    




def getPlotValues(websites):
    # Creating Random numbers for each one
    # x = random.randint(100, size=(len(websites)))
    # x = x.tolist()
    x = []
    dictInfo = {}

    # JSON file
    f = open('cookies.json', "r")

    # Reading from file
    data = json.loads(f.read())

    # Iterating through the json
    # list
    for i in data:
        dataKey = i["host_key"]
        print(dataKey, type(dataKey))
        if dataKey in dictInfo:
            value = dictInfo.get(dataKey)
            value += 1
        else :
            dictInfo[data] = 1

    print(dictInfo)

    # Closing file
    f.close()



    return x


def getAllDomains():
    # Getting all of the websits into an array
    websites = []

    with open("domains.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            websites.append(stripped_line)
    
    return websites




def main():
    # print("Hey")
    websites = getAllDomains()
    values = getPlotValues(websites)
    createPlot(websites, values)



main()
