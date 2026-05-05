/*
https://leetcode.com/problems/container-with-most-water/description/
*/

class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     * Time complexity O(n), Space complexity O(1)
     */
    maxArea(heights) {
        var l = 0;
        var r = heights.length - 1;

        var res = 0;

        while (l < r){
            res = Math.max(res, Math.min(heights[l], heights[r]) * (r - l));

            if (heights[l] < heights[r]){
                l ++;
            } else{
                r --;
            }
        }

        return res;
    }
}
