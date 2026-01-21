"""
https://leetcode.com/problems/partition-array-for-maximum-sum/description/
"""

class MyInefficientSolution: #Time complexity O(k^n), Space complexity O(n)
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        res = 0

        def dfs(i, cur):
            nonlocal res
            
            if i >= len(arr):
                res = max(cur, res)
                return

            maxVal = 0
            for j in range(i, min(i+k, len(arr))):
                maxVal = max(maxVal, arr[j])
                dfs(j+1, cur + (maxVal * (j-i+1)))


        dfs(0, 0)
        return res

class EfficientSolution: #Time complexity O(n*k), Space complexity O(n)
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = { len(arr) : 0 }

        def dfs(i):
            if i in cache:
                return cache[i]

            cur_max = 0
            res = 0
            for j in range(i, min(len(arr), i + k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                res = max(res, dfs(j + 1) + cur_max * window_size)

            cache[i] = res
            return res

        return dfs(0)


        
