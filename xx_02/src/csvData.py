import csv
import municipality
import disease

def importLocationData (csvFileLongName):
    try:
        csvfile = open(csvFileLongName, 'rt')
    except:
        print("LocationData :: File not found")
    csvReader = csv.reader(csvfile, delimiter=",")
    for row in csvReader:
        municipality.registerMunicipality(row[0], row[1], row[2], row[3])

def importPopulationData (csvFileLongName):
    try:
        csvfile = open(csvFileLongName, 'rt')
    except:
        print("LocationData :: File not found")
    csvReader = csv.reader(csvfile, delimiter=",")
    for row in csvReader:
        municipality.registerPopulation(row[0], row[1], row[2], row[3])

def importDiseaseData (csvFileLongName):
    try:
        csvfile = open(csvFileLongName, 'rt')
    except:
        print("DiseaseData :: File not found")
    csvReader = csv.reader(csvfile, delimiter=",")
    for row in csvReader:
        municipality.registerDisease(row[0], row[1], row[2])
