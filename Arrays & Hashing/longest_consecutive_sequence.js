/*
https://leetcode.com/problems/longest-consecutive-sequence/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     * Time complexity O(n), Space complexity O(n)
     */
    longestConsecutive(nums) {
        const hashset = new Set(nums)
        var res = 0

        for(let i = 0; i < nums.length; i++){
            if(!hashset.has(nums[i] - 1)){
                let count = 1
                let cur = nums[i] + 1

                while(hashset.has(cur)){
                    count += 1
                    cur += 1
                }

                res = Math.max(res, count)
            }
        }

        return res
    }
}
