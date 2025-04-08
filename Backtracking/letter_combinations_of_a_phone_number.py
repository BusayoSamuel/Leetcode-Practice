"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class MySolution: 
    """
    Time complexity O(n * 4^n) = O(4^n)  because for each letter you have 4 choices so 4^n and then each combination is joined before append to to the res list so n 
    Space complexity O(n * 4^n) = O(4^n) as 4^n is the total number of combinations and each combination is a length n
    """
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

        
