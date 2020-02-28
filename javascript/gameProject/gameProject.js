var counts = [0,0,0,0,0,0,0,0,0]
var one = document.getElementById('11')
var two = document.getElementById('12')
var three = document.getElementById('13')
var four = document.getElementById('21')
var five = document.getElementById('22')
var six = document.getElementById('23')
var seven = document.getElementById('31')
var eight = document.getElementById('32')
var nine = document.getElementById('33')


var cells = [one, two, three, four, five, six, seven, eight, nine]

function listen(c){
  c.addEventListener("click", function(){
  counts[0] += 1;
  if (counts[0] % 3 == 1){
    c.textContent = 'X'
  }
  else if (counts[0] % 3 == 2){
    c.textContent = 'O'
  }
  else{
    c.textContent = ''
  }
})
}


cells.forEach(listen)
