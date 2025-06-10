"""
https://leetcode.com/problems/find-unique-binary-string/description/
"""

class MySolution: #Time complexity O(2^n), Space complexity O(n)
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        res = ""

        def backtrack(curS):
            nonlocal n
            nonlocal nums
            nonlocal res

            if len(curS) == n:
                s = "".join(curS) 
                if s not in nums:
                    res = s
                    return True
                return False

            for i in range(2):
                c = str(i)
                curS.append(c)
                if backtrack(curS):
                    return True
                curS.pop()

        backtrack([])
        return res


class OtherSolution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        strSet = { s for s in nums }
        
        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res
            
            res = backtrack(i+1, cur)
            if res: return res
            
            cur[i] = "1"
            res = backtrack(i+1, cur)
            if res: return res
            
        return backtrack(0, ["0" for s in nums])


class MyOtherSolution: #Same complexity as above
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hashset = set(nums)
        cur = []
        n = len(nums)

        def dfs(n):
            if len(cur) == n:
                print(cur)
                num = "".join(cur)
                if num not in hashset:
                    return num
                else:
                    return False

            cur.append('0')
            res = dfs(n)
            if res:
                return res

            cur.pop()
            cur.append('1')
            res = dfs(n)
            if res:
                return res
            cur.pop()


        return dfs(n)

            

        
        
