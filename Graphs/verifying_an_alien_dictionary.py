"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

class MySolution: #Time complexity O(n*m) where n is the len(words) and m is the max len(word), Space complexity O(1) as there are only 26 characters 
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i, c in enumerate(order):
            hashmap[c] = set([*order[i:]])
            hashmap[c].add(' ')
        hashmap[' '] = set([*order]+[' '])

        i = 0
        cur = ' '
        for i, word in enumerate(words):
            j = 0
            while i > 0 and j < len(word) and j < len(words[i-1]) and word[j] == words[i-1][j]:
                cur = words[i-1][j]
                j += 1
                
            if j >= len(word) and j < len(words[i-1]):
                return False
            
            if j >= len(words[i-1]):
                cur = word[0]
                continue

            c = word[j]
            if c not in hashmap[cur]:
                return False
            cur = c

        return True

class CleanerSolution: #Same complexity
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # first differing char
        # if word A is prefix of word B, word B must be AFTER word A
        orderInd = { c : i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        return True


        
