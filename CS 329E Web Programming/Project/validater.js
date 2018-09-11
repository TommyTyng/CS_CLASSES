function validater(){
    console.log('validater online');
    var zipcode = document.JTT.zipcode.value;
    var email = document.JTT.email.value;
    var rezipcode = /^\d{5}$/;
    var reemail =/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(rezipcode.test(zipcode) && reemail.test(email)){
        window.alert("You are all signed up!");
    }else{
        window.alert("Not a valid zipcode or email adrress. Try again!");
    }
}