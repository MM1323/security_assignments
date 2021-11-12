import json
import matplotlib.pyplot as plt
from numpy import random
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def createThirdPartyPlots(values):
    # Creates the plot of all third party cookies
    fig = plt.figure(figsize=(100, 20))
    State = [key for key, value in values.items()]
    growth = [value for key, value in values.items()]


    # Create a pandas dataframe
    df = pd.DataFrame({"Domain": State,
                    "Number of Cookies": growth})


    # sort dataframe
    df.sort_values('Number of Cookies')


    # make barplot and sort bars
    sns.barplot(x='Domain',
                y="Number of Cookies", data=df,
                order=df.sort_values('Number of Cookies').Domain)

    # Format the x-axis
    fig.autofmt_xdate()

    # Save Image
    plt.savefig('thirdparty.png')

    # Show the Graph
    # plt.show() 


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
    State = [key for key, value in values.items()]
    growth = [value for key, value in values.items()]

    # Create a pandas dataframe
    df = pd.DataFrame({"Domain": State,
                    "Number of Cookies": growth})


    # sort dataframe
    df.sort_values('Number of Cookies')


    # make barplot and sort bars
    sns.barplot(x='Domain',
                y="Number of Cookies", data=df,
                order=df.sort_values('Number of Cookies').Domain)
    
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


def main():
    # Getting all the domains visited
    websites = getAllDomains()

    # Plot Creation for visited domains
    values = getDomainPlotValues(websites)
    createCookiesPlot(values)

    # Plot Creation for all cookies
    thirdPartyValues = getThirdPartyPlots()
    createThirdPartyPlots(thirdPartyValues)

    
main()