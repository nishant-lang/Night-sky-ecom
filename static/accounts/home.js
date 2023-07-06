
function validateEmail(){
	
	var emailInput = document.getElementById('email');
	var emailError = document.getElementById('req-email');
	if (emailInput.value.trim() === '') {
		emailError.innerHTML = 'This field is required.';
		emailInput.focus();

	}else{
		emailError.innerHTML = '';
	}
}

function validateUsername(){

	var emailInput = document.getElementById('username');
	var emailError = document.getElementById('username-required');

	if (emailInput.value.trim() === '') {
		emailError.innerHTML = 'This field is required.';
		emailInput.focus();

	}else{
		emailError.innerHTML = '';
	}
}

function validatePassword(){
	var emailInput = document.getElementById('password');
	var emailError = document.getElementById('pass-required');

	if (emailInput.value.trim() === '') {
		emailError.innerHTML = 'This field is required.';
		emailInput.focus();
	}else{
		emailError.innerHTML = '';
	}
}

function validatePassword2(){

	var emailInput = document.getElementById('password2');
	var emailError = document.getElementById('pass2-required');

	if (emailInput.value.trim() === '') {
		emailError.innerHTML = 'This field is required.';
		emailInput.focus();

	}else{
		emailError.innerHTML = '';
	}
}

function getdata(){
	var email=document.getElementById('email').value;
	var username=document.getElementById('username').value;
	var password=document.getElementById('password').value;
	var password2=document.getElementById('password2').value;
	var gender = document.querySelector('input[name="gender"]:checked').value;
	var is_retailer = document.querySelector('input[name="retailer"]:checked').value;
	var city=document.getElementById('city').value;
	var state=document.getElementById('state').value;
	var pincode=document.getElementById('pincode').value;

	const email_required=document.getElementById('req-email')
	const username_required=document.getElementById('username-required');
	const pass_required=document.getElementById('pass-required')
	const pass2_required=document.getElementById('pass2-required')
	
	if (email.trim()===''){
		alert('You must Enter email')
	}
	if (username.trim()===''){
		alert('You must Enter username')
	}

	if (password.trim()===''){
		alert('You must Enter password')
	}

	if (password2.trim()===''){
		alert('You must Enter Confirm password')
	}

	if (city.trim() === '') {
		city = "null";
	  }
	  
	if (state.trim() === '') {
		state = "null";
	  }
	  
	if (pincode.trim() === '') {
		pincode = "null";
	  }
   
	var csrfToken=`{{csrf_token}}`

	data={email:email,username:username,gender:gender,city:city,state:state,pincode:pincode,is_retailer:is_retailer,password:password,password2:password2}
	 

	fetch(`http://127.0.0.1:8000/registration/`,{

		method:"POST",
		headers:{'X-CSRFToken':'{{csrf_token}}',"Content-Type":"application/json"},
		body:JSON.stringify(data),
		credential:'same-origin',
		
	}).then(response => {
		console.log(response.status)
		return response.json()
		//return get_blog_post()
	
	}).then((data)=>{
		//console.log(data)
		if (data.hasOwnProperty('message')){
			var model_ele=document.getElementById('model-data');
			var img = document.getElementById("image-id");
			var submit_tag=document.getElementById("submit-tag")
			var okay_btn=document.getElementById("okay-btn")
			var close_btn=document.getElementById("modal-close")
			close_btn.style.display = "none";

			okay_btn.href = "login/"; 
			submit_tag.innerHTML="Form Submitted!";
			img.src="static/vendors/images/success.png";
			model_ele.innerHTML=data['message'];
			$('#success-modal').modal('show');
		}

		if (data.hasOwnProperty('regd_pass_errors')){
			//console.log(data.regd_pass_errors);
			if (data.regd_pass_errors === "You are already registered.") {
				var button = document.getElementById('cross-button');
				button.style.display = 'block';
				var okay_btn=document.getElementById("okay-btn")
				okay_btn.href = "login/";
				okay_btn.innerHTML="Login"
				var close_btn=document.getElementById("modal-close")
				close_btn.style.display = "none";
				model_ele=document.getElementById('model-data')
				model_ele.innerHTML=data.regd_pass_errors
				$('#success-modal').modal('show'); 
			}else{
				var element = document.getElementById("okay-btn");
				element.style.display = "none";
				model_ele=document.getElementById('model-data')
				model_ele.innerHTML=data.regd_pass_errors
				$('#success-modal').modal('show');
			}
		} 
		
		if (data.hasOwnProperty('email')) {
			console.log(data.email[0])
			email_required.innerHTML = data.email[0]	
		} 

		if (data.hasOwnProperty('username')){
			username_required.innerHTML = data.username[0]
		}

		if (data.hasOwnProperty('password')){
			pass_required.innerHTML = data.password[0]
		}

		if (data.hasOwnProperty('password2')){
			pass2_required.innerHTML = data.password2[0]
		}
	})
	}

