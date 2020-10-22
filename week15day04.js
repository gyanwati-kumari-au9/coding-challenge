//Q. Create a Javascript program that generates the difference of two strings using Hamming distance
// algorithm.
function hamming(str,str1){
    var i = 0;
    var count = 0;
    if (str.length != str1.length){
        return "NotHamming"
    }
    for (i = 0; i < str.length; i++){
            if (str[i] != str1[i]){
                count += 1;
            }
    }
    return count;
}
var name = "gyanabt"
var name1 = "gyanibn"
res = hamming(name,name1);
console.log("hamming distance :"+res);

