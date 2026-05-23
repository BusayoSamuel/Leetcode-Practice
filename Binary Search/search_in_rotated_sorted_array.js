/*
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        var l = 0
        var r = nums.length - 1

        while(l<=r){
            var m = Math.floor((r+l)/2)

            if(nums[m] === target){
                return m
            }

            if(nums[m] < nums[r]){
                if(nums[m] < target && target <= nums[r]){
                    l = m + 1
                }else{
                    r = m - 1
                }
            }else{
                if(nums[l] <= target && target < nums[m]){
                    r = m - 1
                }else{
                    l = m + 1
                }
            }
        }

        return -1
    }
}
