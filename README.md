# Generate_GraphML-file
Create a GraphML file for yEd editor

objective - to construct items05.graphml in repo

PS the variable are ~variablesname~

header-

<?xml version="1.0" encoding="UTF-8" standalone="no"?>

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
  <graph edgedefault="directed" id="G">

nodes template- the variables need to be replaced with values and appended to the file after header
        vars - ~NodeNum~ incremented for every node EX:n1,n2...
               ~NodeName~ is user given input EX: Router,Switch...
               ~imageid~ is selected from footer based in type  
    <node id="n~NodeNum~">
      <data key="d3"><![CDATA[~NodeName~]]></data>
      <data key="d6">
        <y:SVGNode>
          <y:Geometry height="13.801994323730469" width="42.398406982421875" x="306.1889221296983" y="371.7524306"/>
          <y:Fill color="#CCCCFF" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="33.40234375" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="72.02734375" x="-14.814468383789062" y="17.80199432373047">~NodeName~
            <y:LabelModel>
              <y:SmartNodeLabelModel distance="4.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="-0.5" nodeRatioX="0.0" nodeRatioY="0.5" offsetX="0.0" offsetY="4.0" upX="0.0" upY="-1.0"/>
            </y:ModelParameter>
          </y:NodeLabel>
          <y:SVGNodeProperties usingVisualBounds="true"/>
          <y:SVGModel svgBoundsPolicy="0">
            <y:SVGContent refid="~imageid~"/>
          </y:SVGModel>
        </y:SVGNode>
      </data>
    </node>
    
    edge template - the variables need to be replaced with values and appended to the file after nodes
    
     
    <edge id="e~id~" source="n~Nodeid~" target="n~Nodeid~">
      <data key="d10">
        <y:PolyLineEdge>
          <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>
