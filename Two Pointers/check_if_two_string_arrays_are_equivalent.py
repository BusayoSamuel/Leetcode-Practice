"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
"""

class MySolution1: #Time complexity O(n), #Space complexity O(n)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = "".join(word1)
        word2 = "".join(word2)

        return word1 == word2

class MySolution2: #Time complexity O(n), #Space complexity O(n)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        stack = []
        
        for i in range(len(word1)):
            for j in range(len(word1[i])):
                stack.append(word1[i][j])

        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word2[i]) - 1, -1, -1):
                if stack[-1] != word2[i][j]:
                    return False

                stack.pop()
        return not stack

class EfficientSolution: #Time complexity O(n), #Space complexity O(1)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = 0
        j1 = 0
        i2 = 0
        j2 = 0

        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False

            if j1 == len(word1[i1]) - 1:
                i1 += 1
                j1 = 0
            else:
                j1 += 1

            if j2 == len(word2[i2]) - 1:
                i2 += 1
                j2 = 0
            else:
                j2 += 1


        return i1 == len(word1) and i2 == len(word2)

        
        
