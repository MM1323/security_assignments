import pandas as pd
import numpy as np
from io import StringIO
import scipy.stats
import scipy
import os
import sys
import warnings
warnings.filterwarnings('ignore')


def main():
    data = "placeholder"
    if (len(sys.argv) > 1):
        data = pd.read_csv(sys.argv[1])
    else:
        # If no command line arguement is passed
        data = pd.read_csv("lCensusData.csv")

    # Make so that it t closeness
    wasserstein = tCloseness(data)

    # Print the distance
    print(wasserstein)

""" 
Group them 
Get the distance for each group and compare to the whole one
Keep the max of distance
Return that max
"""
def tCloseness(data):
    group = data.groupby(['Occupation', 'Age','Race', 'Sex', 'HoursPerWeek'])
    eduSet = data['EducationNum']

    returnVal= 0

    for item in group.groups.keys():
        groupEduNum = group.get_group(item)['EducationNum']
        dist = scipy.stats.wasserstein_distance(eduSet, groupEduNum)
        if (dist > returnVal):
            returnVal = dist

    return returnVal

""" Call on main"""
if __name__ == "__main__":
    main()