// Given a string, determine if it is a palindrome, considering only alphanumeric characters
// and ignoring cases.
// Note: For the purpose of this problem, we define empty string as valid palindrome.
// Example 1:
// Input: "A man, a plan, a canal: Panama"
// Output: true
// Example 2:
// Input: "race a car"
// Output: false
// Constraints:
// • s consists only of printable ASCII characters.

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var i = 0;
    var j = s.length - 1;
    var m = '';
    var n = '';
    while (i < j) {
      m = s[i].toLowerCase();
      n = s[j].toLowerCase();
      if (!isLetterOrDigit(m)) i++;
      else if (!isLetterOrDigit(n)) j--;
      else if (m === n) { i++; j--; }
      else return false;
    }
    return true;
  };
  
  var isLetterOrDigit = function (c) {
    return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
  };

  str = "A man, a plan, a canal: Panama";
  console.log(isPalindrome(str));
  str1 = "race a car";
  console.log(isPalindrome(str1));