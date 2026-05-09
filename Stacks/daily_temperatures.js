/*
https://leetcode.com/problems/daily-temperatures/description/
*/


class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     * Time complexity O(n), Space complexity O(n)
     */
    dailyTemperatures(temperatures) {
        const res = new Array(temperatures.length).fill(0)
        const stack = []

        for(let i = 0; i < temperatures.length; i++){
            while(stack.length && stack[stack.length - 1][0] < temperatures[i]){
                const [temp, j] = stack.pop()
                res[j] = i - j
            }
            stack.push([temperatures[i], i])
        }

        return res
    }
}
