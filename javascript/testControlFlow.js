var temp = prompt("Enter the temperature in celcius: ")

if (!temp){
  alert("NO TEMPERATURE PROVIDED")
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
