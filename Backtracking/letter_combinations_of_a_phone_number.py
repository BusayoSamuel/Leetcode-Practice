"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class MySolution: #Time complexity O(4^n), Space complexity O(4^n)
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        res = []
        curS = []

        def backtrack(pos):

            if pos >= len(digits):
                if curS:
                    res.append("".join(curS))
                return

            for letter in hashmap[digits[pos]]:
                curS.append(letter)
                backtrack(pos + 1)
                curS.pop()
        
        backtrack(0)
            
        return res
        