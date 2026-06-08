/*
https://leetcode.com/problems/product-of-array-except-self/description/
*/

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     * Time complexity O(n), Space complexity O(1)
     */
    productExceptSelf(nums) {
        const prefix = Array(nums.length).fill(1);
        const postfix = Array(nums.length).fill(1);

        let curr = 1
        for(let i = 0; i < nums.length; i++){
            curr = curr * nums[i];
            prefix[i] = curr;
        }

        curr = 1
        for(let j = nums.length - 1; j > -1 ; j--){
            curr = curr * nums[j];
            postfix[j] = curr;
        }

        const res = Array(nums.length).fill(1)
        for(let k = 0; k < nums.length; k++){
            let pre = k-1 >= 0 ? prefix[k-1] : 1;
            let post = k + 1 < nums.length ? postfix[k+1] : 1;

            res[k] = pre * post;
        }

        return res
    }
}
