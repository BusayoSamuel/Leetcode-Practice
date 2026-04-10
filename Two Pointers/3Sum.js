/*
https://neetcode.io/problems/three-integer-sum/question
*/

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     * Time compplexity O(n^2), Space complexity O(n) due to sorting
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b)
        let res = []

        for(let i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] === nums[i-1]){
                continue;
            }
            let j = i + 1
            let k = nums.length - 1

            while(j < k){
                let total = nums[i] + nums[j] + nums[k]

                if(total > 0){
                    k -= 1
                }else if(total < 0){
                    j += 1
                }else{
                    res.push([nums[i], nums[j], nums[k]])
                    j += 1
                    while(j < k && nums[j] === nums[j-1]){
                        j += 1
                    }
                }
            }
        }
        return res
    }
}
