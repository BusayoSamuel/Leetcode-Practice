/*
https://leetcode.com/problems/combination-sum-ii/description/
*/

class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     * Time complexity O(n * 2^n), Space complexity O(n)
     */
    combinationSum2(candidates, target) {
        candidates.sort()
        const res = []
        const cur = []

        function dfs(i, total){
            if(total === target){
                res.push([...cur])
            }

            if(i > candidates.length || total > target){
                return
            }

            for(let j = i; j < candidates.length; j++ ){
                if(j > i && candidates[j] == candidates[j-1]){
                    continue
                }

                cur.push(candidates[j])
                dfs(j + 1, total + candidates[j])
                cur.pop()
            }
        }

        dfs(0, 0)
        return res
    }
}
