from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryMonitor.Definition import *


__doc__ = """snChasFanMap

snChasFanMap detects Chassis Fans for Foundry Devices.

"""

class snChasFanMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snChasFanDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'snChasFanEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.1.3.1.1'
    snmpIndexName = 'snChasFanIndex'
    snmpTitleName = 'snChasFanDescription'
    snmpMonitorName = 'snChasFanOperStatus'
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
            name = 'fan-%s' % snmpindex #getattr(om, self.snmpIndexName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex #getattr(om, self.snmpIndexName)
            rm.append(om)
        maps.append(rm)
        return maps

