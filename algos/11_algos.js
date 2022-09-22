/* 
Given an int to represent how much change is needed
calculate the fewest number of coins needed to create that change,
using the standard US denominations
*/
// quarter = 25 cents, dime = 10, nickel = 5, penny = 1
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    //Your code here

    let coins = {}

    while (cents >= 25){
        coins['quarter'] ? coins['quarter']++ : coins['quarter'] = 1;
        cents -= 25
    }
    while (cents >= 10){
        coins['dime'] ? coins['dime']++ : coins['dime'] = 1;
        cents -= 10
    }
    while (cents >= 5){
        coins['nickel'] ? coins['nickel']++ : coins['nickel'] = 1;
        cents -=5
    }
    while (cents>= 1){
        coins['penny'] ? coins['penny']++ : coins['penny'] = 1;
        cents -=1
    }
    // let filtered_coins = Object.keys(coins).filter(coin=>coins[coin] != 0)
    // // return filtered_coins
    // let final_coins = {}
    // for (key of filtered_coins){
    //     // console.log(key)
    //     // delete coins[key]
    //     final_coins[key] = coins[key]

    // }
    // return final_coins
    return coins



}

console.log(fewestCoinChange(cents1)) // { quarter: 1 }
console.log(fewestCoinChange(cents2)) // { quarter: 2 }
console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }