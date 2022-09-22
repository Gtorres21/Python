/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    //Your code here
    var reverseWord = "";
    for (var i = str.length - 1; i >= 0; i--){
        reverseWord = reverseWord + str[i];
    }
    return reverseWord
    // var splitStr = str.split(""); //Makes str into Array
    // var reverseArr = splitStr.reverse(); //Makes newArr reverse
    // var joinReverse = reverseArr.join("");

    // console.log(reverseArr)
}
// function reverseString(str) {
//     //Your code here
//     let reversed = ""
//     for (let pineapple of str){
//       // console.log(char)
//       reversed = pineapple + reversed
//     }
//     return reversed
// }

// //TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""