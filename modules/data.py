def interpretData(data):
    # subFunction definintions -------------------------------------------------

    def populatePrototypes():
        prototypes = {}
        for protoName in data['protoNames']:
            prototypes[protoName] = {}
            prototypes[protoName]['fields'] = getFields(protoName)
            prototypes[protoName]['template'] = getTemplate(protoName)
            prototypes[protoName]['variables'] = getVariables(
                prototypes[protoName]['template'])
            prototypes[protoName]['tags'] = getTags(protoName)

            # tests. Throw exception if coupled list lengths do not match
            assert len(prototypes[protoName]['fields']) == len(
                prototypes[protoName]['template'])

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

    def getVariables(template):
        protoIndex = data['protoNames'].index(protoName)
        values = []
        for fieldIndex in range(len(data['fieldNames'])):
            if data['protoFieldValues'][protoIndex][fieldIndex] != None:
                values.append(data['protoFieldValues'][protoIndex][fieldIndex])
        return values

    def getTags(protoName):
        protoDataIndex = data['dataNames'].index('ProtoName')
        tags = []
        for tagIndex, tag in enumerate(data['tagNames']):
            if data['tagDataValues'][protoDataIndex][tagIndex] == protoName:
                tags.append(tag)

        return tags

    def extractVariable(inputString):
        x = inputString
        return x[x.find('##')+2: inputString.rfind('##')]

    # --------------------------------------------------------------------------
    populatePrototypes()
    return data


def packageData(data):
    return data
