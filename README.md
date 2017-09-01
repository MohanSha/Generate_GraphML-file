# Generate_GraphML-file
Create a GraphML file for yEd editor

objective - to construct items05.graphml in repo

        PS the variable are ~variablesname~

header- available in repo named header.txt
        
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


nodes template- the variables need to be replaced with values and appended to the file after header
         			
     vars - ~NodeNum~ incremented for every node EX:n1,n2...
            ~NodeName~ is user given input EX: Router,Switch...
            ~imageid~ is selected from footer based in type  
   
    
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

footer- available in repo named footer.txt
