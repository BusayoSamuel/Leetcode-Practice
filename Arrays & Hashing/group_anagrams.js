/*
https://leetcode.com/problems/group-anagrams/description/
*/


class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     * Time complexity O(m*n), Space complexity O(m*n) where m is the number of strs and n is the length of the longest s
     */
    groupAnagrams(strs) {
        const map = new Map();

        for (let s of strs){
            const count = new Array(26).fill(0);
            for(let c of s){
                count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }
            const key = count.join(',');
            if (!map.has(key)) {
                map.set(key, []);
            }
            map.get(key).push(s);
        }

        return [...map.values()]
    }
}
