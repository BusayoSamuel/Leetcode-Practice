"""
https://leetcode.com/problems/combinations/description/
"""


class MySolution: #Time complexity O(n*2^k) because branching is 2^k and this is done for all n values, Space complexity O(2^k) as 2^k is the maximum number of possible combinations
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        curSet = []
        
        def decide(idx):

            if len(curSet) == k:
                res.append(curSet.copy())
                return

            if idx >= len(nums):
                return

            #branching starts here
            curSet.append(nums[idx])
            decide(idx + 1)
            curSet.pop()

            decide(idx+1)

        decide(0)
        return res
    
 #Time complexity O(kn^k) or O(nCk), Space complexity O(kn^k) ot O(nCk)
class AnotherSolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                helper(i+1, comb)
                comb.pop()
        helper(1, [])
        return res

        