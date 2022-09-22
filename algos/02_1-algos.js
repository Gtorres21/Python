/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const str3 = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expectedD = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
 function join(arr, separator) {
    //Your code here
    let joined = "";
    for (let i = 0; i < arr.length; i++) {
        joined += arr[i];
        if (i < arr.length - 1) {
            joined += separator;
        }
    }
    return joined;
}

function acronymize(str) {
    //Your code here
    let acronym = "";
    let words = str.split(" ");
    for (let i = 0; i < words.length; i++) {
        if (words[i] !== "") {
            acronym += words[i][0].toUpperCase();
        }
    }
    return acronym;
}

function acronymize2(str) {
    //Your code here
    let acronym = "";
    let currentWord = "";
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            currentWord += str[i];
        } else if (currentWord.length > 0) {
            acronym += currentWord[0];
            currentWord = "";
        }
    }
    if (currentWord.length > 0) {
        acronym += currentWord[0];
    }
    return acronym.toUpperCase();
}
function acronymize(str) {
    //Your code here
    let newStr = ""
    if(str[0] != " "){
        newStr += str[0]
    }
    for(let j =0; j <str.length; j++){
        if(str[j-1]==" " && str[j] != " "){
            // console.log(str[j+1])
            newStr += str[j]
            // console.log(newStr)
            // console.log(str[j-1])
        // }
        }
    // 
    }
    return newStr.toUpperCase()
}

console.log(acronymize(str1)); // Expected: "OOP"
console.log(acronymize(str2)); // Expected: "APIE"
console.log(acronymize(str3)); // Expected: "SDLC"
console.log(acronymize(str4)); // Expected: "GIT"