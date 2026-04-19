/*
https://leetcode.com/problems/koko-eating-bananas/description/
*/


class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     * Time complexity O(log(max(piles)*len(piles)), Space complexity O(1)
     */
    minEatingSpeed(piles, h) {
        function calcTime(k){
            let t = 0
            for(var pile of piles){
                t += Math.ceil(pile/k)
            }
            return t
        }

        let l = 1
        let r = Math.max(...piles)
        var res = r

        while (l <= r){
            let m = Math.floor((l + r)/2)

            if (calcTime(m) > h){
                l = m + 1
            }else{
                res = m
                r = m - 1
            }
        }
        return res

    }
}
