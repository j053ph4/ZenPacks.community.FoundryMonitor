
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.snChasPwrSupplyPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'snChasPwrSupply',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "getSensorState"
                    }, 
                    {
                        "name": "snChasPwrSupplyDescription"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Sensor State", 
                        "renderer": "pass_link", 
                        "id": "getSensorState", 
                        "dataIndex": "getSensorState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Description", 
                        "renderer": "pass_link", 
                        "id": "snChasPwrSupplyDescription", 
                        "dataIndex": "snChasPwrSupplyDescription"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.snChasPwrSupplyPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('snChasPwrSupplyPanel', ZC.snChasPwrSupplyPanel);
    ZC.registerName('snChasPwrSupply', _t('Power Supply'), _t('Power Supplies'));
    
    })();

