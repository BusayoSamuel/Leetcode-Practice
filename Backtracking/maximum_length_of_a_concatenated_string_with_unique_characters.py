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


class AlternativeSolution: #Same complexity
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1
            # prev = set()
            # for c in s:
            #     if c in charSet or c in prev:
            #         return True
            #     prev.add(c)
            # return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))  # dont concatenate arr[i]

        return backtrack(0)


class AlternativeSolution: #Same complexity
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1
            # prev = set()
            # for c in s:
            #     if c in charSet or c in prev:
            #         return True
            #     prev.add(c)
            # return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))  # dont concatenate arr[i]

        return backtrack(0)


class MyOtherSolution: #Same complexity
    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def backtrack(i, unique):
            nonlocal res
            res = max(res, len(unique))

            if i >= len(arr):
                return

            for j in range(i, len(arr)):
                if len(arr[j]) > len(set([*arr[j]])):
                    continue

                for k in range(len(arr[j])):
                    if arr[j][k] in unique:
                        break
                    
                    if k == len(arr[j]) - 1:
                        unique.update([*arr[j]])
                        backtrack(j+1, unique)
                        unique -= set([*arr[j]])

        backtrack(0, set([]))
        return res


class MyOtherSolution:
    def maxLength(self, arr: List[str]) -> int:
        cur = []
        res = 0

        def dfs(i):
            nonlocal res

            s = "".join(cur)
            if len(s) > len(set(s)):
                return

            res = max(res, len(s))

            if i >= len(arr):
                return

            for j in range(i, len(arr)):
                cur.append(arr[j])
                dfs(j+1)
                cur.pop()
            
        dfs(0)
        return res


        
                

            

            
        

		
        
