import modules.config as c
import modules.data as d
import modules.utils as u

if c.io['inputType'] == 'excel':
    import input.fromExcel as i
    params = c.excel
else:
    raise Exception('no valid input source configured')

if c.io['outputType'] == 'dbf':
    import output.toDBF as o
else:
    raise Exception('no valid output format configured')

dataRaw = i.getData(params)
# print(dataRaw)
dataSet = d.interpretData(dataRaw)
pass
