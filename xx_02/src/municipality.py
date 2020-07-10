import county

dictMunicipality = {}
dictPopulation = {}
dictDiseaseDay = {}
dictDiseaseWeek = {}

def registerMunicipality (mCode, mName, cCode, cName):
    if  mCode not in dictMunicipality:
        county.registerCounty (cCode, cName)
        dictMunicipality[mCode]=mName

def registerPopulation (mCode, mYear, tag, dNbrPop):
    if  mYear == "2020":
        stripCode = mCode[2:6]
        dictPopulation[stripCode]=dNbrPop
        
def registerDiseaseDay(date,value,mCode):
    if mCode in dictDiseaseDay:
        if date in dictDiseaseDay[mCode]:
            dictDiseaseDay[mCode][date]+=1
        else:
            dictDiseaseDay[mCode][date]=1
    else:
        dictDiseaseDay[mCode]={}
        dictDiseaseDay[mCode][date]=1
        
        
def registerDiseaseWeek(date,value,mCode):
    stripYear = date[0:4]
    stripWeek = date[5:7] #midlertidig dummydata
    if mCode in dictDiseaseWeek:
        if stripYear in dictDiseaseWeek[mCode]:
            if stripWeek in dictDiseaseWeek[mCode][stripYear]:
                dictDiseaseWeek[mCode][stripYear][stripWeek]+=1
            else:
                dictDiseaseWeek[mCode][stripYear][stripWeek]=1
        else:
            dictDiseaseWeek[mCode][stripYear]={}
            dictDiseaseWeek[mCode][stripYear][stripWeek]=1
    else:
        dictDiseaseWeek[mCode]={}
        dictDiseaseWeek[mCode][stripYear]={}
        dictDiseaseWeek[mCode][stripYear][stripWeek]=1
     
def registerDisease(date,value,mCode):
    if date != "date":
        stripCode = mCode[7:11]
        if value == "1 person":
            registerDiseaseDay(date,value,stripCode)
            registerDiseaseDay(date,value,county.dictCounty[stripCode])
            registerDiseaseDay(date,value,"norge")
            registerDiseaseWeek(date,value,stripCode)
        else:
            print("Disease value "  + value + "  " + mCode)
       
