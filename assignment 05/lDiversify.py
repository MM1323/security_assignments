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













def saveData(data):
    data.to_csv("lCensusData.csv", index=False, encoding='utf8')

if __name__ == "__main__":
    main()