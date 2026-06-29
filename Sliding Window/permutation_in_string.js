/*
https://leetcode.com/problems/permutation-in-string/description/
*/


class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     * Time complexity 0(n), Space complexity O(1)
     */
    checkInclusion(s1, s2) {
        const s1Count = new Map();
        const s2Count = new Map();

        for(const c of s1){
            s1Count.set(c, (s1Count.get(c) || 0) + 1);
        }

        var l = 0;
        for(let r = 0; r < s2.length; r++){
            s2Count.set(s2[r], (s2Count.get(s2[r]) || 0) + 1);

            if(r - l + 1 > s1.length){
                s2Count.set(s2[l], (s2Count.get(s2[l])) - 1);
                if(s2Count.get(s2[l]) === 0){
                    s2Count.delete(s2[l]);
                }
                l += 1;
            }

            if(r - l + 1 === s1.length){
                let match = true;
                if (s1Count.size !== s2Count.size) match = false;
                else {
                    for (let [key, val] of s1Count) {
                        if (s2Count.get(key) !== val) {
                            match = false;
                            break;
                        }
                    }
                }
                if (match) return true;
            }
        }
        return false
    }
}
