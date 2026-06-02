"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution {
    /**
     * @param {string} s
     * @return {number}
     * Time complexity O(n), Space complexity O(n)
     */
    lengthOfLongestSubstring(s) {
        const hashset = new Set();
        var res = 0;
        var l = 0;

        for(let r = 0; r < s.length; r++){
            while(l <= r && hashset.has(s[r])){
                hashset.delete(s[l]);
                l += 1;
            }

            hashset.add(s[r]);
            res = Math.max(res, r - l + 1);
        }

        return res;
    }
}
