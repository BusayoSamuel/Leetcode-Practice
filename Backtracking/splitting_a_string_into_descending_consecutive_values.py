"""
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/description/
"""

class MySolution: #Time complexity O(n^n), Space complexity O(n)
    def splitString(self, s: str) -> bool:
        curSeq = []
        
        def backtrack(i):
            nonlocal curSeq

            if i >= len(s):
                return len(curSeq) > 1

            for j in range(i, len(s)):
                subS = s[i:j+1]
                if not curSeq or int(subS) == curSeq[-1] - 1:
                    curSeq.append(int(subS))
                    if backtrack(j+1):
                        return True
                    curSeq.pop()
            
            return False

        return backtrack(0)


class OtherSolution: #Same complexity as above
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev):
            if index == len(s):
                return True
        
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                if val + 1 == prev and dfs(j+1, val):
                    return True
            return False
    
        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if dfs(i+1, val): return True
                
        return False

class MyOtherSolution: #Same complexity as above
    def splitString(self, s: str) -> bool:
        def dfs(i, target):
            if i >= len(s):
                return True

            for j in range(i, len(s)):
                cur = int(s[i:j+1])
                print(cur)

                if j == len(s)-1 and target == None:
                    return False

                if cur == target or target == None:
                    if dfs(j+1, cur - 1):
                        return True

            return False

        return dfs(0, None)

        
