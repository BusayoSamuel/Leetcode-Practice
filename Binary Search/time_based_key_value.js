"""
https://leetcode.com/problems/time-based-key-value-store/description/
"""


class TimeMap { 
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if(!this.keyStore.get(key)){
            this.keyStore.set(key, [])
        }

        const arr = this.keyStore.get(key)
        arr.push([timestamp, value])

        this.keyStore.set(key, arr)
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     * Time complexity O(logn), Space complexity O(n)
     */
    get(key, timestamp) {
        if(!this.keyStore.get(key)){
            return "";
        }

        var l = 0
        var r = this.keyStore.get(key).length - 1
        var res = ""

        while (l <= r){
            var m = Math.floor((r + l)/2)

            const [time, value] = this.keyStore.get(key)[m]

            if (time > timestamp){
                r = m - 1
            }else if(time < timestamp){
                l = m + 1
                res = value
            }else{
                return value
            }
        }

        return res
    }

}
