"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
"""

class MySolution: #Time complexity O(n^2 + m^2), Space complexity O(n + m)
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        res = []

        for w1 in s1:
            count = 0
            for w in s1:
                if w == w1:
                    count += 1
            if count == 1:
                if w1 not in set(s2):
                    res.append(w1)

        for w2 in s2:
            count = 0
            for w in s2:
                if w == w2:
                    count += 1
            if count == 1:
                if w2 not in set(s1):
                    res.append(w2)

        return res

class BetterSolution: #Time complexity O(n + m) , Space complexity O(n + m)
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        res = []

        for w in (s1 + " " + s2).split(" "):
            if w in hashmap:
                hashmap[w] += 1
            else:
                hashmap[w] = 1

        for w in hashmap.keys():
            if hashmap[w] == 1: #the target values would only appear once in a combination of the two strings
                res.append(w)

        return res