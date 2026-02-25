/*
https://leetcode.com/problems/binary-search/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     * Time complexity O(nlogn) Space complexity O(n)
     */
    search(nums, target) { 
        nums.sort((a, b) => a - b)
        let l = 0
        let r = nums.length - 1

        while ( l <= r){
            let m = Math.trunc((r+l)/2)

            if (nums[m] > target){
                r = m - 1
            } else if (nums[m] < target){
                l = m + 1
            } else {
                return m
            }
        }
        return -1
    }
}
