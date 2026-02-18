/*
https://leetcode.com/problems/valid-palindrome/description/
*/

/**
 * @param {string} s
 * @return {boolean}
 Time complexity O(n) Space complexity O(1)
 */
var isPalindrome = function(s) { 
    let l = 0;
    let r = s.length - 1;
    const isAlnum = /^[a-z0-9]$/i;

    while (l <= r) {

        while (l <= r && !isAlnum.test(s[l])) {
            l++;
        }

        while (l <= r && !isAlnum.test(s[r])) {
            r--;
        }

        if (l <= r && s[l].toLowerCase() !== s[r].toLowerCase()) {
            return false;
        }

        l++;
        r--;
    }

    return true;
    
};
