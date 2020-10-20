var stack = [];
function push(ev){
    
    var elem =document.getElementById('input').value;
    if(document.getElementById("input").value.length == 0)
    {
        alert("Empty value")
        return;
    }
    stack.push(elem);
    document.getElementById("res").innerHTML = stack;
    
}
function pop(ev){
    ev.preventDefault();
    stack.pop();
    document.getElementById("res").innerHTML = stack;
}