import csv

#with open('input.csv') as f:
#    reader = csv.reader(f)
#    for Node_name, Type in reader:
#        print(Node_name, Type)

#def csv_dict_reader(file_obj):
#    reader = csv.DictReader(file_obj, delimiter=',')
#    for line in reader:
#      print(line["Node_name"]),
#      print(line["Type"]),

#if __name__ == "__main__":
#    with open("input.csv") as f_obj:
#       csv_dict_reader(f_obj)

#file = open('head.txt', 'r')
#htext = file.read()
htext="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <!--Created by yEd 3.17-->
  <key for="port" id="d0" yfiles.type="portgraphics"/>
  <key for="port" id="d1" yfiles.type="portgeometry"/>
  <key for="port" id="d2" yfiles.type="portuserdata"/>
  <key attr.name="Name" attr.type="string" for="node" id="d3"/>
  <key attr.name="url" attr.type="string" for="node" id="d4"/>
  <key attr.name="description" attr.type="string" for="node" id="d5"/>
  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="graphml" id="d7" yfiles.type="resources"/>
  <key attr.name="url" attr.type="string" for="edge" id="d8"/>
  <key attr.name="description" attr.type="string" for="edge" id="d9"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <graph edgedefault="directed" id="G"> \n
"""

fname=input("Enter file name to save: ")
f= open(fname+".graphml","a+")         
f.write(htext)

nid=-1
while input("\nEnter Node Y/N: ")=="Y":
    nid+=1
    print("\nNode ID :",nid)
    label=input("Enter Node Name: ")
    resid=input("""Select Resource ID \n1-  Switch  2-  Router  3- VLAN Network  4- Internet  5- Server \nEnter the ID: """)
    node="""
    <node id="n%d">
      <data key="d3"><![CDATA[%s]]></data>
      <data key="d6">
        <y:SVGNode>
          <y:Geometry height="33.801994323730469" width="42.398406982421875" x="-118.29437408411025" y="594.7073565079138"/>
          <y:Fill color="#CCCCFF" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="33.40234375" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="72.02734375" x="-14.814468383789062" y="17.80199432373047">%s
            <y:LabelModel>
              <y:SmartNodeLabelModel distance="4.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="-0.5" nodeRatioX="0.0" nodeRatioY="0.5" offsetX="0.0" offsetY="4.0" upX="0.0" upY="-1.0"/>
            </y:ModelParameter>
          </y:NodeLabel>
          <y:SVGNodeProperties usingVisualBounds="true"/>
          <y:SVGModel svgBoundsPolicy="0">
            <y:SVGContent refid="%d"/>
          </y:SVGModel>
        </y:SVGNode>
      </data>
    </node>
    """
    #print(node)
    f.write(node %(int(nid), label, label, int(resid)))

eid=-1
while input("\nEnter Edge Y/N: ")=="Y":
    
    
    eid+=1
    src=input('\nEnter Source Node ID: ')
    targ=input('Enter Target Node ID: ')
    edge="""
    <edge id="e%d" source="n%d" target="n%d">
      <data key="d10">
        <y:PolyLineEdge>
          <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>
    """
    #print("edge")
    f.write(edge%(int(eid), int(src), int(targ)))


file = open('foot.txt', 'r')
ftext = file.read()
f.write(ftext)



#file.close() #head close
file.close() #foot close
f.close() #graphml close