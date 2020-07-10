'''  ******************************************************************
xx_02, infectious disease surveillance program

uses pandas, openpyxl

Created on 09.jul.2020
@author: abitas
*********************************************************************** '''

import os
import sys
import pandas
import params
import disease
import csvData

def printWelcome():
    try:
        python_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        python_paths = []

        print("Welcome to xx_02, infectious disease surveillance program!")
        print(python_paths)
        print(sys.implementation.name)
        print(sys.implementation.version)

printWelcome()
csvData.importLocationData(params.inputLocationCsvFile)
csvData.importPopulationData(params.inputPopulationCsvFile)
csvData.importDiseaseData(params.inputDeseaseCsvFile)
diseaseTable = {"iso-year":[],"iso-week": []}
dfDisease = pandas.DataFrame(diseaseTable, columns = ['iso-year', 'iso-week'])
disease.writeExcel(dfDisease, params.outputXlsxFile)