import modules.config as c
import modules.data as d
import modules.utils as u

if c.io['inputType'] == 'excel':
    import input.fromExcel as i
    cfgIn = c.excel
else:
    raise Exception('no valid input source configured')

if c.io['outputType'] == 'dbf':
    import output.toDBF as o
    cfgOut = c.dbf
else:
    raise Exception('no valid output format configured')

dataRaw = i.getData(cfgIn)
dataSet = d.interpretData(dataRaw)
dataPackage = d.packageData(dataSet)
# o.createTable(dataPackage, cfgOut)
