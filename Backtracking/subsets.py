"""
https://leetcode.com/problems/subsets/description/
"""


class MySolution: #Time complesity O(2^n), Space complexity O(n2^n) because each array at the bottom of each branch is going to have a max size of n
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def decide(i, curSet):
            nonlocal res

            if i >= len(nums):
                res.append(curSet.copy()) #the same reference is used on each recurcive call so you need to append a copy
                return

            curSet.append(nums[i])
                                    #you dont append the curSet at this stage else you get duplicates
            decide(i + 1, curSet)

            curSet.pop()
                                  #you dont append the curSet at this stage else you get duplicates
            decide(i + 1, curSet)

        decide(0, [])
        return res
    


class CleanerSolution: #Same complexity
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)

        return res
        


            