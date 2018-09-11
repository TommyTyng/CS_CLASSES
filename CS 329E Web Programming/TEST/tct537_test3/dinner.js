document.getElementById("items").maxLength;
document.getElementById("username").maxLength;

function checkItems(items){
  if(document.getElementById("username").value == null || document.getElementById("username").value == "" || document.getElementById("items").value == null || document.getElementById("items").value == ""){
    document.getElementById("submit").disabled = true;
  }else{
    document.getElementById("submit").disabled = false;
  }
}