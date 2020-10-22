// Write a Javascript program that produces a star pattern likes this.
// *
// **
// ***
// ****
// *****
// ****
// ***
// **
// * 
function stars(n){
    var str = '';
    var k = (n+1)/2;
    var m = 1;
    for(var i=1; i<=n+1; i++){
        for(var j=1; j < m; j++){
            str += "*";
        }

        if( i <= k){
            m += 1;
        }
        else {
            m -= 1;
        }
        console.log(str);
        str = "";
    }
}
stars(9);