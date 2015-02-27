from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryMonitor.Definition import *
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryMonitor.Definition import *



__doc__ = """snAgentTempMap

snAgentTempMap detects Temperature Sensors for Foundry Devices.

"""


class snAgentTempMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snAgentTempDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'snAgentTempEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.2.13.1.1'
    snmpIndexName = 'snAgentTempSlotNum'
    snmpTitleName = 'snAgentTempSensorId'
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.3': 'snAgentTempSensorDescr',
            }),
        )
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s", self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpTableName)
        log.debug("table: %s" % trunktable)
        for snmpindex, trunk in trunktable.items():
            log.debug("idx: %s, trunk: %s" % (snmpindex, trunk))
            om = self.objectMap(trunk)
            name = 'tempsensor-%s' % snmpindex
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex
            rm.append(om)
        maps.append(rm)
        return maps

