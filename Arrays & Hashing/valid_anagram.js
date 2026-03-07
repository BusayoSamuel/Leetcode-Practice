// https://leetcode.com/problems/valid-anagram/description/

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     Time complexity O(n), Space complexity O(1)
     */
    isAnagram(s, t) {
        var scount = {}

        for (var c of s){
            scount[c] = (scount[c] ?? 0) + 1
        }

        for (var c of t){
            if (scount[c] !== undefined){
                scount[c] = scount[c] - 1
                if (scount[c] === 0){
                    delete scount[c]
                }
            }else{
                return false
            }
        }

        return Object.keys(scount).length === 0
    }
}
