import dbf


def createTables(dataIn, cfg):
    # subFunction definintions -------------------------------------------------

    def addFieldString(dataSet):
        outputDataSet = dataSet
        for prototype in dataSet:
            fieldList = dataSet[prototype]['fields']
            if fieldList:
                fieldString = ' C(255); '.join(fieldList)+' C(255); '
                outputDataSet[prototype]['fieldString'] = fieldString
            else:
                outputDataSet[prototype]['fieldString'] = None
        return outputDataSet

    def makeDBF(data):
        if data['fieldString']:
            dbfTable = dbf.Table(filename='output/'+data['name'] +
                                 '.dbf', field_specs=data['fieldString'],)
            dbfTable.open(mode=dbf.READ_WRITE)
            for row in data['rows']:
                rowTuple = tuple(row)
                dbfTable.append(rowTuple)
            print(data['name'] + " generated")
        else:
            print(data['name'] + " is empty, no file created")
        pass

    # --------------------------------------------------------------------------

    dataPackage = addFieldString(dataIn)
    for prototype in dataPackage:
        protoData = dataPackage[prototype]
        makeDBF(protoData)
    print('DBFs created')
