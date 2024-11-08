"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(1)
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = defaultdict(list)

        for i, c in enumerate(s):
            indices[c].append(i)

        res = -1

        for key, val in indices.items():
            res = max(res, val[-1]-val[0]-1)

        return res

class CleanerSolution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {} #char -> first index
        res = -1

        for i, c in enumerate(s):
            if c in char_index:
                res = max(res, i - char_index[c] - 1)
            else:
                char_index[c] = i

        return res


        
        


        
