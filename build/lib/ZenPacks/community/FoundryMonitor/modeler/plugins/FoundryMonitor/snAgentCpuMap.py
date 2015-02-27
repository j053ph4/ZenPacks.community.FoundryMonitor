from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FoundryMonitor.Definition import *


__doc__ = """snAgentCpuMap

snAgentCpuMap detects CPUs for Foundry Devices.

"""

class snAgentCpuMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(snAgentCpuDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'snAgentCpuUtilEntry'
    snmpTableOID = '.1.3.6.1.4.1.1991.1.1.2.11.1.1'
    snmpIndexName = 'snAgentCpuUtilSlotNum'
    snmpTitleName = 'snAgentCpuUtilCpuId'
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
            '.3': 'snAgentCpuUtilInterval',
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
            if om.snAgentCpuUtilInterval != 5: continue
            name = "cpu-%s" % snmpindex
            #name = "slot-%s_cpu-%s" % (om.snAgentCpuUtilSlotNum, om.snAgentCpuUtilCpuId)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex #"%s.%s.%s" % ( om.snAgentCpuUtilSlotNum, om.snAgentCpuUtilCpuId,om.snAgentCpuUtilInterval)
            rm.append(om)
        maps.append(rm)
        return maps

