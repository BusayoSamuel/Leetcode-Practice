/*
https://leetcode.com/problems/two-sum/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     * Time complexity O(n), Space complexity O(n)
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; i++){
            if (map.has(target - nums[i])){
                return [map.get(target - nums[i]), i]
            }

            map.set(nums[i], i)
        }
        
    }
}
