// Given a 32-bit signed integer, reverse digits of an integer.
// Example 1:
// Input: 123 Output: 321
// Example 2:
// Input: -123 Output: -321
// Example 3:
// Input: 120 Output: 21
// Rules:
// 1.	No conversion to string and back please.
// This is one of the most common number related question asked in interviews according to TopCoder and LeetCode

var reverse = function(x) {
    const max = Math.pow(2, 31);
    let r = 0;
    while (x !== 0) {
      r = r * 10 + x % 10;
      if (r > max || r < -max) return 0;
      x = (x / 10) << 0;
    }
    
    return r;
  };


rev = 123;
console.log(reverse(rev));