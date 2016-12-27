function find_geometry(value, f) {
	//Dependiendo del elemento que se haya seleccionado, crea una lista con los tipos de incidente correspondientes
	//a ese elemento
	
	if (value=="POINT") {
		var list=new Array();
		list[0]="Select a type of incident";
		list[1]="Benches";
		list[2]="Cash Machine";
		list[3]="Fallen Trees";
		list[4]="Fire Hidrants";
		list[5]="Manholes";
		list[6]="Parking Meter";
		list[7]="Postboxes";
		list[8]="Potholes";
		list[9]="Street Lights";
		list[10]="Street Signs";
		list[11]="Trash Cans";
		list[12]="Traffic Lights";
		list[13]="Water Leaks";
		list[14]="Zombie";
		list[15]="Other";
	}
		
	else if (value=="LINE") {
		var list=new Array();
		list[0]="Select a type of incident";
		list[1]="Road Blocks";
		list[2]="Other";
	}
	
	else if (value=="POLYGON") {
		var list=new Array();
		list[0]="Select a type of incident";
		list[1]="Flooding";
		list[2]="Road Blocks";
		list[3]="Zombie invasion";
		list[4]="Construction Site";
	}
	
	else {
		var list=new Array();
	}
	
	var options='';
		
	//crea el desplegable en html con los valores de las listas
	for (var i = 0; i<list.length; i++) {
		if (list[i]=="Select a type of incident") {
			options+='<option value="none">'+list[i]+'</option>';
		}
		else {
			options+='<option value="'+list[i]+'">'+list[i]+'</option>';
		}
	}
	document.getElementById('type-form').value="geometry";
	if (value!="none") {
    	send_form(f);
    }
	document.getElementById('incident_type').innerHTML=options;
}

function find_type(value, f) {
	document.getElementById('type-form').value="incident_type";
    if (value!="none") {
    	send_form(f);
    }

}