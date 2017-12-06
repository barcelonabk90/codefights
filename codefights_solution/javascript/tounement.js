/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function sequenceElement(a, n) {
    var arr = [];
    for (var i = 0; i < 5; i++) {
        arr.push(a[i]);
    }
    var M = Math.pow(10, 5);
    var cnt = 1;
    var obj = {};
    obj[cnt] = 4;

    for (var i = 5; ; i++) {
        arr.push((arr[i - 1] + arr[i - 2] +
                arr[i - 3] + arr[i - 4] + arr[i - 5]) % 10);
        cnt = (cnt * 10 + arr[i]) % M;
        if (cnt in obj) {
            var last = obj[cnt];
            return arr[n % (i - last)];
        } else {
            obj[cnt] = i;
        }
    }
}

/**
 * We need a function that calculates the number of Sundays after a specific day for a given period.

Example

For n = 9 and startDay = "Saturday", the output should be
howManySundays(n, startDay) = 2;
For n = 7 and startDay = "Sunday", the output should be
howManySundays(n, startDay) = 1.
 * @param {type} n
 * @param {type} startDay
 * @returns {Number}
 */
function howManySundays(n, startDay) {

  var week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday'],
      startIndex;

  for (var i = 0; i < week.length; i++) {
    if (week[i] === startDay) {
      startIndex = i;
    }
  }

  return Math.floor((n + startIndex) / week.length);
}

/**
 * Given a string, find the number of different non-empty substrings in it.

Example

For inputString = "abac", the output should be
differentSubstringsTrie(inputString) = 9.
 * @param {type} a
 * @returns {Number}
 */
function differentSubstringsTrie(a) {
    var arr = [];
    var res = 1;
    var c = a.length;
    for (var i = 0; i < c; i++) {
        for (var j = i + 1; j <= c; j++) {
            arr.push(a.substring(i, j));
        }
    }
    arr.sort();
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[i - 1]) {
            res++;
        }
    }
    return res;
}

/**
 * Given an array of 2k integers (for some integer k), 
 * perform the following operations until the array contains only one element:

On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product.
After the algorithm has finished, there will be a single element left in the array. Return that element.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
arrayConversion(inputArray) = 186.

We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.
 * @param {type} a
 * @returns {arrayConversion.a|@var;arr}
 */
function arrayConversion(a) {
    var k = 0;
    while(a.length > 1){
        var arr = [];
        for(var i = 0; i < a.length-1; i += 2){
            if(k % 2 === 0){
                arr.push(a[i] + a[i+1]);
            }else{
                arr.push(a[i] * a[i+1]);
            }
            
        }
        k++;
        a = arr;
    }
    return a[0];
}

/**
 * Remove all characters from a given string that appear more than once in it.

Example
For str = "zaabcbd", the output should be
removeDuplicateCharacters(str) = "zcd".
 * @param {type} str
 * @returns {String}
 */
function removeDuplicateCharacters(str) {
    var res = "";
    for(var i = 0; i < str.length; i++){
        var flg = 1;
        for(var j = 0; j < str.length; j++){
            if(str[i] === str[j] && i !== j){
                flg = 0;
                break;
            }
        }
        if(flg){
            res += str[i];
        }
    }
    return res;
}

function removeDuplicateCharacters(str) {
    return str
    .split('')
    .filter(function(item, pos, self) {
        // aaabbcde -> return abcde
        //return self.indexOf(item) === pos;
        
        //aaabbcde -> return cde
        var a1 = self.slice(0,pos);
        var a2 = self.slice(pos +1);
        return a1.indexOf(item) < 0 && a2.indexOf(item) < 0;
    })
    .join('');
}

/**
 * Let's say that number a feels comfortable with number b if a ≠ b
 *  and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r],
 and each number feels comfortable with the other?

Example

For l = 10 and r = 12, the output should be
comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:

s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable 
with each other within the segment [10; 12]: (10, 11) and (11, 12).
 * @param {type} l
 * @param {type} r
 * @returns {Number}
 */
function comfortableNumbers(l, r) {
    var sumOfDigit = function(a){
        var r = 0;
        while(a){
            r += a % 10;
            a = Math.floor(a/10);
        }
        return r;
    };
    var comf = function(a, b){
        var s_a = sumOfDigit(a);
        var s_b = sumOfDigit(b);
        return a - s_a <= b && b  <= a + s_a && b - s_b <= a && a <= b + s_b;
    };
    var res = 0;
    for(var i = l; i <= r; i++){
        for(var j = i +1; j <= r; j++){
            if(comf(i,j)){
                res++;
            }
        }
    }
    return res;
}


/**
 * A password is complex enough, if it meets all of the following conditions:

its length is at least 5 characters;
it contains at least one capital letter;
it contains at least one small letter;
it contains at least one digit.
Determine whether a given password is complex enough.

Example

For inputString = "my.Password123", the output should be
passwordCheckRegExp(inputString) = true;
For inputString = "my.password123", the output should be
passwordCheckRegExp(inputString) = false.
 * @param {type} inputString
 * @returns {Number}
 */
function passwordCheckRegExp(inputString) {
    var c = inputString.length;
    if(c < 5){
        return 0;
    }
    var isUpper = function(c){
        return 'A' <= c && c <= 'Z';
        //return c === c.toUpperCase();
    };
    var isLower = function(c){
        return 'a' <= c && c <= 'z';
        //return c === c.toLowerCase();
    };
    var isDigit = function(c){
        return '0' <= c && c <= '9';
        //return !(isNaN(c));
    };
    var upperFlg = 0;
    var lowerFlg = 0;
    var digitFlg = 0;
    for(var i in inputString){
        if(isUpper(inputString[i])){
            upperFlg = 1;
        }
        if(isLower(inputString[i])){
            lowerFlg = 1;
        }
        if(isDigit(inputString[i])){
            digitFlg = 1;
        }
    }
    return upperFlg * lowerFlg * digitFlg;
    
}

/**
 * Define an integer's roundness as the number of trailing zeros in it. 
 * Sometimes it is possible to increase a number's roundness by swapping two of its digits.

Given an integer n, find the minimum number of swaps required to maximize n's roundness.
 * @param {type} n
 * @returns {Number}
 */
function maximizeNumberRoundness(n) {
    var tmp = n ;
    var r = 0;
    while(tmp){
        if(tmp % 10 === 0){
            r++;
        }
        tmp = Math.floor(tmp/10);
        var a = r;
    }
    for(var i = 0; i < a; i++){
        if(n % 10 === 0){
            r--;
        }
        n = Math.floor(n/10);
    }
    return r;
}


