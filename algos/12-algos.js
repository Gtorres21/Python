/* 
Array: Mode

Create a function that, given an array of ints,
returns the int that occurs most frequently in the array.
What if there are multiple items that occur the same number of time?
- return all of them (in an array)
- what if all items occur the same number of times?
    - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1]; // or [1,5]
//  - order doesn't matter


/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
// function mode(nums) {
//     //Your code here
//     if ( nums.length < 2){
//         return nums;
//     }
//     dict = {};
//     for (let index of nums){
//         if (dict[index]){
//             dict[index] += 1;
//         }else{
//             dict[index] = 1;
//         }
//     } // frequency Table
//     let max = 0
//     for(let key in dict){
//         if (dict[key] >= max){
//             max = dict[key]
//         }else{
//             delete[key]
//         }
//     }
//     for (let key in dict){
//         if (dict[key] === max){
//             continue
//         }else{
//             delete dict[key]
//         }
//     }
//     return dict
// }

function mode(nums) {
    if (nums.length === 1 || nums.length === 0) {
        return nums;
    }

    let modes = [];
    let maxCount = 0;
    let allSame = true;
    let freqs = {}

    for (let num of nums){
        freqs[num] = freqs[num] + 1 || 1 ; //builds freq table
        maxCount = Math.max(maxCount, freqs[num]);
    }

    for (let key in freqs){
        if (freqs[key] === maxCount){
            modes.push(parseInt(key));
        }else{
            allSame = false;
        }
    }
    
    return allSame ? [] : modes;
        // expression ? true : false;

}


console.log(mode(nums1)) // []
console.log(mode(nums2)) // [1]
console.log(mode(nums3)) // []
console.log(mode(nums4)) // [1]
console.log(mode(nums5)) // [5, 1]