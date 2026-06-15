/*
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
*/

class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     * Time complexity O(n), Space complexity O(n)
     */
    largestRectangleArea(heights) {
        const stack = []
        var res = 0

        for(let i = 0; i < heights.length; i++){
            let start = i
            while(stack.length && stack[stack.length-1][1] > heights[i]){
                var [index, height] = stack.pop()
                res = Math.max(res, height * (i - index))
                start = index
            }
            stack.push([start, heights[i]])
        }

        const i = heights.length
        while(stack.length){
            var [index, height] = stack.pop()
            res = Math.max(res, height * (i - index))  
        }

        return res
    }
}
