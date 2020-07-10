import os
import pandas
import numpy
import municipality
import matplotlib.pyplot as plt

def registerDisease (mCode):
    print("    " + mCode)

def readExcel(xFileName):
    return pandas.read_excel(xFileName)

def readCsv(xFileName):
    return pandas.read_csv(xFileName,encoding="ISO-8859-1")

def writeExcel(dFrame, xFileName):
    print(os.getcwd() + "    -    " + xFileName)
    dFrame.to_excel(xFileName, sheet_name='aggregated')