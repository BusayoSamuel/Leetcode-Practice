"""
https://leetcode.com/problems/extra-characters-in-a-string/description/
"""

class MySolution: #Inefficient
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        res = math.inf
        
        def backtrack(i, count):
            nonlocal res 
            
            if i >= len(s):
                res = min(res, count)
                return

            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    backtrack(j+1, count)
                else:
                    backtrack(j+1, count + len(s[i:j+1]))

        backtrack(0, 0)
        return res

class MoreEfficientSolution: #Time complexity O(n^2), Space complexity O(n)
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        hashset = set(dictionary)
        dp = {len(s): 0} #Memoization, we use hashset to store the result of subproblems that have been computed already

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1) #we consider the scenario where we have to skip s[i] which is len(s) in worse case
            for j in range(i, len(s)): #we consider all possible substrings that start with s[i]
                if s[i:j+1] in hashset:
                    res = min(res, dfs(j+1)) #therefore we don't have to count those character, we start our search from the next character again
            dp[i] = res #we update the result of this subproblem in our cache
            return res

        return dfs(0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()
        
        for word in dictionary:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True


class MostEfficientSolution: #we enchance the performance of using a set alone
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root #we add our dictionary to the trie
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur.children: #now we're considering each character instead
                    break # we don't have to consider other characters at this point because we know that substrings exist beyond this point
                cur = cur.children[s[j]] #we update cur to next sub-level
                if cur.word:
                    res = min(res, dfs(j+1)) #we only update res if this is a word in the dictionary
                    
            dp[i] = res
            return res

        return dfs(0)
            
            
