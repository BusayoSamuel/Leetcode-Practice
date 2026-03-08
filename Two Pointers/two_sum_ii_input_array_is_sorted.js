//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     Time complexity O(n), Space complexity O(1)
     */
    twoSum(numbers, target) {
        let l = 0
        let r = numbers.length - 1

        while (l <= r){
            let total = numbers[l] + numbers[r]

            if (total > target){
                r -= 1
            } else if ( total < target){
                l += 1
            } else {
                return [l + 1, r + 1]
            }
        }
    }
}
