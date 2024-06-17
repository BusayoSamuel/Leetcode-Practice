"""
https://leetcode.com/problems/number-of-matching-subsequences/description/
"""

class MySolution: #Time complexity O(n*m), Space complexity O(1), where n is the len(s) and m is the number of words
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        for word in words:
            index = -1
            isSub = True
            for c in word:
                index = s.find(c, index + 1)
                if index == -1:
                    isSub = False
                    break
            if isSub:
                count += 1

        return count


class OptimalSolution: #Time complexity O(w * m * n), Space complexity O(1), where w is the length of the average word
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        for word in words:
            index = -1
            isSub = True
            for c in word:
                index = s.find(c, index + 1) #yet because the find function is interpreted in C by the python interpreter, this code perform quicker
                if index == -1:
                    isSub = False
                    break
            if isSub:
                count += 1

        return count
                
                
