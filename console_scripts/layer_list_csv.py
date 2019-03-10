group_name = "group_name"
csv_path = "/path/to/table.csv"

root = QgsProject.instance().layerTreeRoot()

group_layers = []
for i in root.findGroup(group_name).findLayers():
    group_layers.append(i.layerId())

    layer = i.layer()
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    renderer = QgsRuleBasedRenderer(symbol)
    root_rule = renderer.rootRule()
    rule = root_rule.children()[0]
    rule.setLabel("Atlas")
    rule.setFilterExpression('@layer_id =  @atlas_pagename')
    layer.setRenderer(renderer)

with open(csv_path, "w") as f:
    for item in group_layers:
        f.write("%s\n" % item)
