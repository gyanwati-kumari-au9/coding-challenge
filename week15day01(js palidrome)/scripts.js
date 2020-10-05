var frm = document.getElementById("form");
frm.onsubmit = function (){
    var user = document.getElementById("number").value;
    var view = document.getElementById("result");
    if (isPalidrome(user)){
        result.innerHTML = "This is palidrome" ;
        return false;
    }
    else{
        result.innerHTML = "This is not palidrome" ;
        return false;
    }
}

function isPalidrome(str){
    var arr = str.split("");
    var rev = arr.reverse().join("");
    return rev == str;
}

// console.log(isPalidrome("madam"))