function capitalizeFLetter() { 
    var input = document.getElementById("input"); 
    var x = document.getElementById("div"); 
    var string = input.value; 
    x.innerHTML = string[0].toUpperCase() +  
      string.slice(1).toLowerCase(); 
  } 

