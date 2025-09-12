"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

class MySolution: #Time complexity O(m*n), Space complexity O(1) since we have at most 26 characters
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = Counter(p)
        l = 0
        r = 0
        res = []


        while r < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] -= 1

            while r - l + 1 > len(p):
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                l += 1

            if max(hashmap.values()) == min(hashmap.values()) == 0:
                res.append(l)

            r += 1
        return res

class EfficientSolution: #Time complexity O(m+n), Space complexity O(1) since we have at most 26 characters
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1+ sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1+ sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res

        
