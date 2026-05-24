/*
https://leetcode.com/problems/encode-and-decode-strings/description/
*/

class Solution { 
    constructor(){
        this.hashmap = new Map();
        this.pointer = 0;
    }

    /**
     * @param {string[]} strs
     * @returns {string}
     #Time complexity O(n), Space complexity O(n)
     */
    encode(strs) {
        var res = ""

        for(let s of strs){
            res += String(this.pointer)
            res += ","
            this.hashmap.set(this.pointer, s)
            this.pointer += 1
        }     

        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const res = []

        for(let c of str.split(",").slice(0, -1)){
            res.push(this.hashmap.get(Number(c)))
        }

        return res
    }
}
