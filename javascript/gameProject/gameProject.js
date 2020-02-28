var cell = document.querySelectorAll('td')
var clickCount = 0


function countClickOnCell(c){
  c.addEventListener('click', function(){
    clickCount+=1;
    if (clickCount%3 == 1){
      c.textContent = 'X';
    }
    else if (clickCount%3 == 2){
      c.textContent = 'O';
    }
    else {
      c.textContent = '';
    }
  })
}

cell.forEach(countClickOnCell)
