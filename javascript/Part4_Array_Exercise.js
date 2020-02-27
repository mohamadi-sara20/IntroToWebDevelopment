// PART 4 ARRAY EXERCISE
var roster = []

function addNew(studentName){
  roster.push(studentName);
  return roster;
}


function remove(studentName){
  ind = roster.indexOf(studentName);
  if (ind > -1) {
  roster.splice(ind, 1);
}
  return roster;
}


function display(){
  alert("Please check the console logs for the names!")
  roster.forEach(console.log.bind(console))
}

// Start by asking if they want to use the web app
cont = prompt("Do you want to use the web app? If yes, type 'yes'. If no, type 'no'.")

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (true){

  if (cont == 'no'){
    alert('Thanks! Please refresh the page if you change your mind!');
    break;
  }
  else if (cont == 'yes'){
    action = prompt("Do you want to add, remove, display or quit?");
    if (action == "add"){
      studentName = prompt("What name would you like to add?");
      addNew(studentName);
    }
    else if(action == "remove"){
      studentName = prompt("What name would you like to remove?");
      remove(studentName);
    }
    else if(action=='display'){
      display();
    }
    else if(action=='quit'){
      alert("Thanks! Please refresh if you need to use the app again!");
      break;
    }
    else {
      action = prompt("Do you want to add, remove, display or quit?");
    }
  }
  else{
    cont = prompt("Do you want to use the web app? If yes, type 'yes'. If no, type 'no'.")
  }
}
