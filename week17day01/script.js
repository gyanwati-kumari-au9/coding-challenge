
function calculatorRes(choice){
    var n1=parseFloat(document.getElementById('num1').value);
    var n2=parseFloat(document.getElementById('num2').value);
    var res;
    var c=choice;
    switch(c)
        {
        case '1':
            res=n1+n2;
            document.getElementById('result').innerHTML=res;
            break;
        case '2':
            res=n1-n2;
            break;
        case '3':
            res=n1*n2;

            break;
        case '4': 
            res=n1/n2;
            break;
        default:
            break;
                
        }
    document.getElementById('result').value=res;
    
}