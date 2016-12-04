function initialize() {
  $('nav#menu a').click(click_menu); //Adds an onClick function in each a
  //inside of nav id=menu with the click_menu function
  loadmap();
}

var url="http://localhost/worldwideGeomatics/"

function click_menu() {
	//alert('Click menu: '+this.id);
	var option='application='+this.id;
	
	menu_active(this.id); //This line changes the class active when click on
	
	//This changes the map on display or not
	if (this.id!='home' && this.id!='create' && this.id!='editing') {
		document.getElementById('sec_map').style.display = 'none';
	}
	else {
		document.getElementById('sec_map').style.display = 'block';
	}
	
	$.ajax({
		type: "GET",
		url: url,
		data: option, //Adjuntar los campos del formulario enviado
		success: replace_section
	});		
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
		success: replace_section,
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

function send_logout() {
	document.getElementById('login_li').style.display='block';
	
	document.getElementById('logout_li').style.display = 'none';
}

$(document).ready(initialize); //Execute the function initialize when the
//document is completely loaded