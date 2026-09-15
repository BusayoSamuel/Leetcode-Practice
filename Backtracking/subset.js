/*
https://leetcode.com/problems/subsets/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     * Time complexity O(2^n), Space complexity O(n*2^n)
     */
    subsets(nums) {
        const cur = []
        const res = []

        function backtrack(i){
            if(i >= nums.length){
                res.push([...cur])
                return
            }

            cur.push(nums[i])
            backtrack(i+1)

            cur.pop()
            backtrack(i+1)
        }

        backtrack(0)
        return res
    }
}
