var temp = prompt("Enter the number of temperature in celcius: ")

if (!temp){
  alert("NO TEMPERATURE PROVIDED")
}
else{
  temp = parseInt(temp)
  if(Number.isNaN(temp)){
    alert("THIS IS NOT A NUMBER! PLEASE REFRESH AND ENTER A ***NUMBER****")
  }

  else if (temp> 40.5){
    alert("HOT")
  }
  else if (temp >= 20){
    alert("LUKEWARM")
  }
  else{
    alert("COLD")
  }
}
