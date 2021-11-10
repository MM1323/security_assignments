import json
import matplotlib.pyplot as plt
from numpy import random
import matplotlib.ticker as mticker


def createThirdPartyPlots(values):
    # Creates the plot of all third party cookies
    # Get all x and y values
    xAxis = [key for key, value in values.items()]
    yAxis = [value for key, value in values.items()]

    ## Bar Vertical Graph ##
    plt.bar(xAxis, yAxis, color='maroon')
    # plt.barh(xAxis, yAxis, color='maroon') DELETE LATER
    # plt.xticks(rotation=90) #rotate till sidways
    plt.xlabel('Domain')
    plt.ylabel('Number of Cookies')
    plt.title("Third Party Cookies")

    # Save Image
    plt.savefig('thirdparty.png')

    # Show the Graph
    plt.show() 


def getThirdPartyPlots():
    # A Dictionary of All Third Party domain names and how many there are
    dictInfo = {}

    # JSON file
    f = open('cookies.json', "r")

    # Reading from file
    data = json.loads(f.read())

    # Iterating through the json
    for i in data:
        dataKey = i["host_key"]
        if dataKey in dictInfo:
            value = dictInfo.get(dataKey)
            value += 1
            dictInfo[dataKey] = value
        else :
            dictInfo[dataKey] = 1

    # Closing file
    f.close()

    return dictInfo


def createCookiesPlot(values):
    # Creates the plot of all cookies visited
    xAxis = [key for key, value in values.items()]
    yAxis = [value for key, value in values.items()]

    ## Bar Horizontal Graph ##
    fig = plt.figure()
    plt.barh(xAxis, yAxis, color='maroon')
    plt.xlabel('Number of Cookies')
    plt.ylabel('Domain')
    plt.title("First Party Cookies")
    
    # Save the graph
    plt.savefig('firstparty.png')

    # plt.show()


def getDomainPlotValues(websites):
    # A Dictionary of all domain names and how many there are
    dictInfo = {}

    # JSON file
    f = open('cookies.json', "r")

    # Reading from file
    data = json.loads(f.read())

    # Iterating through the json
    for i in data:
        dataKey = i["host_key"]
        if dataKey in websites: # Only add the ones on the list
            if dataKey in dictInfo:
                value = dictInfo.get(dataKey)
                value += 1
                dictInfo[dataKey] = value
            else :
                dictInfo[dataKey] = 1

    # Closing file
    f.close()

    return dictInfo


def getAllDomains():
    # Getting all of the websits into an array
    websites = []

    with open("domains.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            websites.append(stripped_line)
    
    return websites


def createPlot(websites, values):
    # Basic Plot Creation
    # Actual plot creation
    plt.style.use('ggplot')

    x_pos = [i for i, _ in enumerate(websites)]
    plt.bar(x_pos, values, color='green')

    plt.xlabel("Domain")
    plt.ylabel("Number of Cookies")
    plt.title("First Party Cookies")
    plt.xticks(x_pos, websites)

    # Save the plot
    plt.savefig('test.png')
    # plt.show()


def main():
    # Getting all the domains visited
    websites = getAllDomains()

    # Plot Creation for visited domains
    values = getDomainPlotValues(websites)
    createCookiesPlot(values)

    # Plot Creation for all cookies
    thirdPartyValues = getThirdPartyPlots()
    createThirdPartyPlots(thirdPartyValues)

    # createPlot(websites, values) Old Way



main()
