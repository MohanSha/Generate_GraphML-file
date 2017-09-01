# Generate_GraphML-file
Create a GraphML file for yEd editor

objective - to construct items05.graphml in repo

PS the variable are ~variablesname~

header- available in repo named header.txt


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
