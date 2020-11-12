//  Q. Create a JavaScript program to decode hashes as backspaces and return the
// deleted string.
// Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is
// "bd" Your task is to process a string with "#" symbols.
// (Note: ES6 is must)
// Examples: "abc#d##c" ==> "ac" "abc##d######" ==> "" "#######" ==> "" "" ==> ""

const decodeHashes_Backspace = (str)=>{
    for(var i =0; i <= str.length; i++){
        if (str[i] == "#"){
            str.slice(i);
            str.slice(i-1);
            // str.substr(str[i],str[i-1]);
            // str.replace(str[i-1],'');
            str.replace('#','');
            return str;
        }  
    }
}
h="abc#d##c";
console.log(decodeHashes_Backspace(h));