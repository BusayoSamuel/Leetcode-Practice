"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
"""

class MySolution: #Time complexity O(nm), Space Complexity O(m) where n is the number of words and m is the average length of a word
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            curCount = count.copy()
            good = True
            for c in word:
                if c in curCount and curCount[c] > 0:
                    curCount[c] -= 1
                else:
                    good = False
                    break
            if good:
                res += len(word)

        return res

        
            
