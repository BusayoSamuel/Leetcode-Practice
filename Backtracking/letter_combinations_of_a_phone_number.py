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


class OtherSolution: #Same complexity as above
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

        
