"""
https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
"""


class MySolution: #Time complexity O(n), Space complexity O(1)
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        res = ""

        while l < len(num):
            r = l
            while r+1 < len(num) and num[r+1] == num[l]:
                r += 1

            if r - l >= 2:
                if not res or int(res) < int(num[l:l+3]):
                    res = num[l:l+3]
                l = r - 1    

            l += 1
     
        return res


class CleanerSolution: #Same complexity
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])

        return res



        
