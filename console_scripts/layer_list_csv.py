group_name = "group1"
csv_path = ""

if csv_path == "":
    csv_path = QgsProject.instance().readPath("./") + "/group1_layers.csv"

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

uri = (
    'file://{}?type=csv&delimiter=%20&useHeader=No&detectTypes=yes'
    '&geomType=none&subsetIndex=no&watchFile=no'
).format(csv_path)

layer = iface.addVectorLayer(
    uri, group_name + "_list", "delimitedtext"
)
