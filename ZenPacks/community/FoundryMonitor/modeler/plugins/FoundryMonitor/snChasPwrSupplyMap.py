from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryMonitor.Definition import *

__doc__ = """snChasPwrSupplyMap

snChasPwrSupplyMap detects Power Supplies for Foundry Devices.

"""

class snChasPwrSupplyMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snChasPwrSupplyDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'snChasPwrSupplyEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.1.2.1.1'
    snmpIndexName = 'snChasPwrSupplyIndex'
    snmpTitleName = 'snChasPwrSupplyDescription'
    snmpMonitorName = 'snChasPwrSupplyOperStatus'
    snmpMonitorFlagExists = True
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
            '.3': snmpMonitorName,
            }),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpTableName)
        for snmpindex, trunk in trunktable.items():
            log.debug("idx: %s, trunk: %s" % (snmpindex, trunk))
            om = self.objectMap(trunk)
            name = "pwr-%s" % snmpindex # getattr(om, self.snmpIndexName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex # getattr(om, self.snmpIndexName)
            rm.append(om)
        maps.append(rm)
        return maps

