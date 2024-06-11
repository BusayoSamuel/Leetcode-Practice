"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
"""


class MySolution: #Time complexity O(2^n), Space complexity O(2^n)
    def maxLength(self, arr: List[str]) -> int:
        curSet = []
        res = 0

        def backtrack(i):
            nonlocal res

            temp = "".join(curSet)

            if len(temp) > len(set([*temp])):
                return
            
            if i >= len(arr):
                res = max(res, len(temp))
                return

            curSet.append(arr[i])
            backtrack(i + 1)

            curSet.pop()

            backtrack(i + 1)

        backtrack(0)
        return res


class BetterSolution: #Time complexity O(2^n), Space complexity O(2^n) not n^2 because uniqElements can grow to the size of 2^n
    def maxLength(self, arr: List[str]) -> int:
        
        uniqELements = ['']
        maximum = 0
        for i in range(len(arr)):
            sz = len(uniqELements)
            for j in range(sz):
                x=arr[i]+uniqELements[j]
                if (len(x)==len(set(x))):
                    uniqELements.append(x)
                    maximum = max(maximum,len(x))

        return maximum
		
        
