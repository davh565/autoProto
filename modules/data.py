varErrorStr = '<ERROR: Variable Not Found>'


def interpretData(data):
    prototypes = {}
    # subFunction definintions -------------------------------------------------

    def populatePrototypeData(data):
        for protoName in data['protoNames']:
            prototypes[protoName] = {}
            p = prototypes[protoName]
            p['name'] = protoName
            p['fields'] = getFields(protoName)
            p['template'] = getTemplate(protoName)
            p['variableMask'] = getVariableMask(p['template'])
            p['variableNames'] = getVariableNames(p['template'])
            p['tags'] = getTags(protoName)
            p['variableData'] = getVariableData(p['variableNames'], p['tags'])
            p['rows'] = getRows(
                p['fields'],
                p['template'],
                p['variableMask'],
                p['variableNames'],
                p['tags'],
                p['variableData'])

    def getFields(protoName):
        protoIndex = data['protoNames'].index(protoName)
        fields = []
        for fieldIndex, field in enumerate(data['fieldNames']):
            if data['protoFieldValues'][protoIndex][fieldIndex] != None:
                fields.append(field)

        return fields

    def getTemplate(protoName):
        protoIndex = data['protoNames'].index(protoName)
        values = []
        for fieldIndex in range(len(data['fieldNames'])):
            if data['protoFieldValues'][protoIndex][fieldIndex] != None:
                values.append(data['protoFieldValues'][protoIndex][fieldIndex])
        return values

    def getVariableMask(template):
        values = []
        for value in template:
            e = extractVariable(str(value))
            if e != str(value):
                values.append(True)
            else:
                values.append(False)
        return values

    def getVariableNames(template):
        values = []
        for value in template:
            e = extractVariable(str(value))
            if e != str(value):
                values.append(e)
        return values

    def getTags(protoName):
        protoDataIndex = data['dataNames'].index('ProtoName')
        tags = []
        for tagIndex, tag in enumerate(data['tagNames']):
            if protoName in str(data['tagDataValues'][protoDataIndex][tagIndex]):
                tags.append(tag)

        return tags

    def getVariableData(variables, tags):
        variableData = {}
        for variable in variables:
            if variable in data['dataNames']:
                varIndex = data['dataNames'].index(variable)
                variableData[variable] = []
                for tag in tags:
                    tagLookup = data['tagNames'].index(tag)
                    datum = data['tagDataValues'][varIndex][tagLookup]
                    variableData[variable].append(datum)
        return variableData

    def getRows(
            fields, template, variableMask, variableNames, tags, variableData):
        rows = []
        for tagIndex, tag in enumerate(tags):
            variableIndex = 0
            cols = []
            for fieldIndex, field in enumerate(fields):
                if variableMask[fieldIndex]:
                    variable = variableNames[variableIndex]
                    if variable in data['dataNames']:
                        cols.append(str(variableData[variable][tagIndex]))
                        variableIndex += 1
                    else:
                        cols.append(varErrorStr)
                else:
                    if template[fieldIndex] is None:
                        cols.append(None)
                    else:
                        cols.append(str(template[fieldIndex]))
            rows.append(cols)
        return rows

    def extractVariable(inputString):
        x = inputString
        if '##' in inputString:
            return x[x.find('##')+2: inputString.rfind('##')]
        else:
            return inputString

    def packageProtoData(protoData):
        packagedData = {}
        for proto in protoData:
            packagedData[proto] = {}
            packagedData[proto]['name'] = protoData[proto]['name']
            packagedData[proto]['fields'] = protoData[proto]['fields']
            packagedData[proto]['rows'] = protoData[proto]['rows']
        return packagedData

    # --------------------------------------------------------------------------
    populatePrototypeData(data)

    return packageProtoData(prototypes)

