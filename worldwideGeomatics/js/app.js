function initialize() {
  $('nav#menu a').click(click_menu); //Adds an onClick function in each a
  //inside of nav id=menu with the click_menu function
  loadmap();
}

var url="http://localhost/worldwideGeomatics/"
point=false;
line=false;
polygon=false;

function click_menu() {
	//alert('Click menu: '+this.id);
	var option='application='+this.id;
	
	menu_active(this.id); //This line changes the class active when click on
	
	$.ajax({
		type: "GET",
		url: url,
		data: option, //Adjuntar los campos del formulario enviado
		success: replace_section
	});
	
	//This changes the map on display or not
	if (this.id!='home' && this.id!='create' && this.id!='editing') {
		document.getElementById('sec_map').style.display = 'none';
		document.getElementById('sec_legend').style.display = 'none';
	}
	else {
		document.getElementById('sec_map').style.display = 'block';
		document.getElementById('sec_legend').style.display = 'block';
	}
	
	return false; //Evitar ejecutar el submit del formulario.
}

function replace_section(data) {
	var section=$("#general_section");
	section.replaceWith(data)	
}

//This function changes the active class from one item to the clicked one
function menu_active(id) {
	$('nav#menu li').removeClass('active')
	if (id!="register" && id!="web" && id!="about") {
		id=id;
	}
	else if (id=="register") {
		id="login"
	}
	
	else {
		id="about"
	}
	document.getElementById(id+"_li").className='active'	
}

function send_form(f) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	var v=$(f).serialize() //It extracts the values of the formular and introduce them
						   //like an string on the variable v
						   //serialize has not into account the dissabled fields.
						   //serialize is a JQUERY method.
	$.ajax({
		type: "POST",
		url: url,
		//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
		data: v, //Another way to do it
		success: create_tables,
		error:function (xhr, ajaxOptions, thrownError) {
		alert(xhr.status + '\n' + thrownError);
		}
		});
	return false; //Avoid to execute the submit of the formular
}

function send_login(f) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	var v=$(f).serialize() //It extracts the values of the formular and introduce them
						   //like an string on the variable v
						   //serialize has not into account the dissabled fields.
						   //serialize is a JQUERY method.
	
	//This changes the logout on display or not
	document.getElementById('login_li').style.display='none';
	
	document.getElementById('logout_li').style.display = 'block';
	
	
	$.ajax({
		type: "POST",
		url: url,
		//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
		data: v, //Otr forma de adjuntarlos
		success: replace_section,
		error:function (xhr, ajaxOptions, thrownError) {
		alert(xhr.status + '\n' + thrownError);
		}
		});
	return false; //Avoid to execute the submit of the formular
}

function send_register(f) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	var validate=validateRegister();
	
	if (validate==true) {
		var v=$(f).serialize() //It extracts the values of the formular and introduce them
		   //like an string on the variable v
		   //serialize has not into account the dissabled fields.
		   //serialize is a JQUERY method.

		$.ajax({
		type: "POST",
		url: url,
		//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
		data: v, //Otr forma de adjuntarlos
		success: check_user,
		error:function (xhr, ajaxOptions, thrownError) {
		alert(xhr.status + '\n' + thrownError);
		}
		});
		return false; //Avoid to execute the submit of the formular
	} else {
		pass;
	}
}

function validateRegister() {
	var name=document.getElementById("name");
	var surname=document.getElementById("surname");
	var birth=document.getElementById("birth");
	var country=document.getElementById("country");
	var pc=document.getElementById("pc");
	var tel=document.getElementById("tel");
	var mail=document.getElementById("mail");
	var user=document.getElementById("user");
	var pass=document.getElementById("pass");
	var terms=document.getElementById("terms");
	
	if (name.checkValidity()==false) {
		alert("Name: "+name.validationMessage);
		return false;
	} else if (surname.checkValidity()==false) {
		alert("Surname: "+surname.validationMessage);
		return false;
	} else if (birth.checkValidity()==false) {
		alert("Birth: "+birth.validationMessage);
		return false;
	} else if (country.checkValidity()==false) {
		alert("Country: "+country.validationMessage);
		return false;
	} else if (pc.checkValidity()==false) {
		alert("Postal Code: "+pc.validationMessage);
		return false;
	} else if (tel.checkValidity()==false){
		alert("Phone Number: "+tel.validationMessage+" (Format: +(99)999999999)");
	} else if (mail.checkValidity()==false) {
		alert("E-mail: "+mail.validationMessage);
		return false;
	} else if (user.checkValidity()==false) {
		alert("User: "+user.validationMessage+" (Only Characters. Min 6, Max 15)");
		return false;
	} else if (pass.checkValidity()==false) {
		alert("Password: "+pass.validationMessage+" (Min 6, Max 10, lower and upper case and number)");
		return false;
	} else if (terms.checkValidity()==false) {
		alert("You must accept our Terms of Use");
		return false;
	} else {
		return true;
	}
	
	
}

function send_logout() {
	document.getElementById('login_li').style.display='block';
	
	document.getElementById('logout_li').style.display = 'none';
}

function create_tables(data) {
	var response=$.parseJSON(data);
	
	if (response.selection=="#tables" ||  response.selection=="#final_id"){
		var body=$(response.selection);
		body.replaceWith(response.html);
		if (response.selection=="#final_id"){
			document.getElementById('final_id').style.display = 'block';
		}
	}
	if (response.extension!='null'){
		var extension=$.parseJSON(response.extension);
		zoom(extension.coordinates);
	}
	
	if(response.menu_option=="editing_li"){
		if(response.values!='null'){
			document.getElementById('admin_id').value=response.values[0];
			document.getElementById('old_type_admin').value=response.values[1];
			document.getElementById('old_desc_admin').value=response.values[2];
			if(response.table_selected!='null'){
				document.getElementById('table_selected').value=response.table_selected;
			}
			if(response.incident_type!='null'){
				generate_new_incidents(response.incident_type)
			}
		}
	}
}

function send_geometry(f, info) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	if (info=="geometry"){
		document.getElementById('type-form').value='geometry';
	}
	else if (info=="point") {
		document.getElementById('type-form').value='point';	
	}
	else if (info=="line") {
		document.getElementById('type-form').value='line';
	}
	else if (info=="polygon") {
		document.getElementById('type-form').value='polygon';
	}
		
	
	var v=$(f).serialize() //It extracts the values of the formular and introduce them
	   //like an string on the variable v
	   //serialize has not into account the dissabled fields.
	   //serialize is a JQUERY method.

	$.ajax({
	type: "POST",
	url: url,
	//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
	data: v, //Otr forma de adjuntarlos
	success: generate_incidents,
	error:function (xhr, ajaxOptions, thrownError) {
	alert(xhr.status + '\n' + thrownError);
	}
	});
	return false; //Avoid to execute the submit of the formular	
}

function generate_incidents(data) {
	var response=$.parseJSON(data);
	if (response.geom_type!='null'){
		var types=response.geom_type;
		var list=new Array();
		list[0]="Select a type of incident";
		for (var i = 0; i<types.length; i++) {
			list[i+1]=types[i][0].toString();
		}
		var options='';
		for (var j = 0; j<list.length; j++) {
			if (list[j]=="Select a type of incident") {
				options+='<option value="none">'+list[j]+'</option>';
			}
			else {
				options+='<option value="'+list[j]+'">'+list[j]+'</option>';
			}
		}
		
		document.getElementById('incident_type').innerHTML=options;
	}
	if (response.last_id!='null'){
		var current_id=parseInt(response.last_id)+parseInt(1);
		document.getElementById('id').value=current_id;
	}
	if (response.extension!='null'){
		var extension=$.parseJSON(response.extension);
		zoom(extension.coordinates);
	}
}

function generate_new_incidents(data) {
	var response=data;
	if (response!='null'){
		var types=response;
		var list=new Array();
		list[0]="Select a type of incident";
		for (var i = 0; i<types.length; i++) {
			list[i+1]=types[i][0].toString();
		}
		var options='';
		for (var j = 0; j<list.length; j++) {
			if (list[j]=="Select a type of incident") {
				options+='<option value="none">'+list[j]+'</option>';
			}
			else {
				options+='<option value="'+list[j]+'">'+list[j]+'</option>';
			}
		}
		
		document.getElementById('type_admin').innerHTML=options;
	}
}

function zoom_type(f) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	document.getElementById('type-form').value="incident_type";
	var v=$(f).serialize() //It extracts the values of the formular and introduce them
	   //like an string on the variable v
	   //serialize has not into account the dissabled fields.
	   //serialize is a JQUERY method.

	$.ajax({
	type: "POST",
	url: url,
	//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
	data: v, //Otr forma de adjuntarlos
	success: zoom_to_type,
	error:function (xhr, ajaxOptions, thrownError) {
	alert(xhr.status + '\n' + thrownError);
	}
	});
	return false; //Avoid to execute the submit of the formular	
}

function zoom_to_type(data) {
	var response=$.parseJSON(data);
	if (response.extension!='null'){
		var extension=$.parseJSON(response.extension);
		
		zoom(extension.coordinates);
		
	}
}

function check_user(data) {
	var response=$.parseJSON(data)
	
	if (response.existing=="email") {
		alert("This E-Mail is already registered");
	} else if (response.existing=="username") {
		alert("This username is already registered");
	} else {
		var section=$("#general_section");
		section.replaceWith(response.html)
	}
}

function zoom(bbox) {
	if(bbox.length<2){
		map.getView().fit([bbox[0][0][0],bbox[0][0][1],bbox[0][2][0],bbox[0][2][1]], map.getSize());
	}
	else{
		map.getView().setCenter([bbox[0],bbox[1]]);
		map.getView().setZoom(18);
	}
}

function button_search(f){
	if (document.getElementById('final_id').value!="iniciated"){
		document.getElementById('type-form').value="send"
	}
	else{
		document.getElementById('type-form').value="search"		
	}
	send_form(f)
}

function reset_form(f) {
	var text='<select id="final_id" name="final_id" required><option value="iniciated">Select an ID</option></select>'
	var cuerpo=$('#final_id');
	cuerpo.replaceWith(text)
	document.getElementById('final_id').style.display = 'none';	
}

//**************************** CREATION FORM ***********************************
function send_create(f) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	document.getElementById('type-geometry').value=geometry[0]
	var v=$(f).serialize() //It extracts the values of the formular and introduce them
	   //like an string on the variable v
	   //serialize has not into account the dissabled fields.
	   //serialize is a JQUERY method.

	$.ajax({
	type: "POST",
	url: url,
	//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
	data: v, //Otr forma de adjuntarlos
	success: check_create,
	error:function (xhr, ajaxOptions, thrownError) {
	alert(xhr.status + '\n' + thrownError);
	}
	});
	return false; //Avoid to execute the submit of the formular	
}

function check_create(data) {
	var response=$.parseJSON(data);
	if(response.hack!='null'){
		var hack_alert=response.hack;
		alert(hack_alert);
	}
	if(response.geometry!='null'){
		alert(response.geometry);
	}
	if(response.created!='null'){
		alert(response.created);
	}
}



function set_geometry(f){
	if (geometry[0].length>0) {
		document.getElementById('type-geometry').value=geometry[0];
	}
}

function click_table(value, type){
	var menu_option=document.getElementsByClassName("active")[0].id
	var sentence = "name_form=click_table&result="+String(value)+"&type_table="+type+"&menu_option="+menu_option;
	send_click(sentence)
}

function send_click(sentence) {
	$.ajax({
		type: "POST",
		url: url,
		//data: $(nombre_form).serialize(), //Adjuntar los campos del formulario enviado.
		data: sentence, //Otr forma de adjuntarlos
		success: create_tables,
		error:function (xhr, ajaxOptions, thrownError) {
		alert(xhr.status + '\n' + thrownError);
		}
		});
	return false; //Evitar ejecutar el submit del formulario
}

//**************************** EDDITING FORM ***********************************
function send_edit(f, info) {
	//Here you don't have the acces to 'this' because the event onClick is launched
	//from html; for that it receives f; this is the formular of the button from which 
	//the event onClick is launched.
	//it can't be done from the initialize function because the formular is not created
	//yet, because it's created by ajax, after loading the main page
	if (info=="update"){
		document.getElementById('option').value='update';
	}
	else if (info=="delete") {
		document.getElementById('option').value='delete';	
	}

	var myform=$(f);
	var disabled=myform.find(':input:disabled').removeAttr('disabled');
	var serialized=$(f).serialize(); //It extracts the values of the formular and introduce them
	   //like an string on the variable v
	   //serialize has not into account the dissabled fields.
	   //serialize is a JQUERY method.
	disabled.attr('disabled','disabled');

	$.ajax({
		type: "POST",
		url: url,
		//data: $(nombre_form).serialize(), //Add the fields of the sended formular.
		data: serialized, //Otr forma de adjuntarlos
		success: check_edit,
		error:function (xhr, ajaxOptions, thrownError) {
		alert(xhr.status + '\n' + thrownError);
		}
		});
		return false; //Avoid to execute the submit of the formular	
}

function check_edit(data) {
	var response=$.parseJSON(data);
	if(response.message!='null'){
		alert(response.message);
	}
	if(response.updated!='null'){
		var text=response.updated;
		alert(text);
	}
	if(response.deleted!='null'){
		var text=response.deleted;
		alert(text);
	}
}

$(document).ready(initialize); //Execute the function initialize when the
//document is completely loaded