var emailField = document.getElementById("email");
emailField.addEventListener("change",function() {
	var email = emailField.value;
	if (email == null || email == "") {
		return;
	}
	var xhr; 
	if (window.ActiveXObject) { 
		xhr = new ActiveXObject ("Microsoft.XMLHTTP"); 
	} else if (window.XMLHttpRequest) { 
		xhr = new XMLHttpRequest (); 
	}
	var url = "checkEmail.php";
	var params = "email=" + escape(email);
	
	// Open a connection to the server 
	xhr.open("POST",url,true);
	
	// Create the proper headers to send with the request
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	// Setup a function for the server to run when it is done 
	xhr.addEventListener("load", responseReceivedHandler);

	// Send the request 
	xhr.send(params);
	console.log('email changed');

});

function responseReceivedHandler() {
	if (this.readyState == 4 && this.status == 200) { 
		document.getElementById("message").innerHTML = this.responseText;
	} 
} 