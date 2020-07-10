dictCounty = {}
lastCounty = ""

def registerCounty (cCode, cName):
    if  cCode != lastCounty:
        if  cCode not in dictCounty:
            dictCounty[cCode]=cName
            print("    " + cName)
