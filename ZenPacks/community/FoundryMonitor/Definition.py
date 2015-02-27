from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "FoundryMonitor"
VERSION = Version(1, 0, 0)


def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try: return map[int(ob.getRRDValue(datapoint))]
    except: return 'unknown'
    
def getSensorState(ob): return ob.getMapValue('sensorStatus_sensorStatus', ob.sensorStatusMap)

sensorStatusMap = { 1: 'other', 2: 'normal', 3: 'failure'}

snChasPwrSupplyDefinition = type('snChasPwrSupplyDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snChasPwrSupply',
        'componentData' : {
                          'singular': 'Power Supply',
                          'plural': 'Power Supplies',
                          'displayed': 'snChasPwrSupplyDescription', # component field in Event Console
                          'primaryKey': 'snChasPwrSupplyDescription',
                          'properties': {
                                        'snChasPwrSupplyDescription' : addProperty('Description', optional=False),
                                        'getSensorState' : getReferredMethod('Sensor State', 'getSensorState'),
                                        },
                          },
        'componentAttributes' : {'sensorStatusMap': sensorStatusMap },
        'componentMethods' : [getMapValue, getSensorState]
        })

snChasFanDefinition = type('snChasFanDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snChasFan',
        'componentData' : {
                          'singular': 'Fan',
                          'plural': 'Fans',
                          'displayed': 'snChasFanDescription', # component field in Event Console
                          'primaryKey': 'snChasFanDescription',
                          'properties': {
                                        'snChasFanDescription' : addProperty('Description', optional=False),
                                        'getSensorState' : getReferredMethod('Sensor State', 'getSensorState'),
                                        },
                          },
        'componentAttributes' : {'sensorStatusMap': sensorStatusMap },
        'componentMethods' : [getMapValue, getSensorState]
        })

snAgentCpuDefinition = type('snAgentCpuDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snAgentCpu',
        'componentData' : {
                          'singular': 'Processor',
                          'plural': 'Processors',
                          'displayed': 'id', # component field in Event Console
                          'primaryKey': 'id',
                          'properties': {
                                        'snAgentCpuUtilSlotNum' : addProperty('Slot Number', optional=False),
                                        'snAgentCpuUtilCpuId' : addProperty('CPU ID', optional=False),
                                        },
                          },
        'componentMethods' : [],
})


snAgentTempDefinition = type('snAgentTempDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'snAgentTemp',
        'componentData' : {
                          'singular': 'Temp Sensor',
                          'plural': 'Temp Sensors',
                          'displayed': 'snAgentTempSensorDescr', # component field in Event Console
                          'primaryKey': 'snAgentTempSensorDescr',
                          'properties': {
                                        'snAgentTempSlotNum' : addProperty('Slot Number', optional=False),
                                        'snAgentTempSensorId' : addProperty('Sensor ID', optional=False),
                                        'snAgentTempSensorDescr' : addProperty('Description', optional=False),
                                        },
                          },
        'componentMethods' : [],                                                        
})

