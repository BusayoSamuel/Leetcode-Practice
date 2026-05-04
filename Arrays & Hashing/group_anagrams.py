"""
https://leetcode.com/problems/group-anagrams/description/
"""

class Solution: #Time complexity O(m * n), Space complexity O(m * n) where m is the number of strs and n is the length of the longest str
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


class MySolution: #Inefficient
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashset = set()

        def isAnagram(s1, s2):
            hashmap = {}

            if len(s1) != len(s2):
                return False
            
            for i in range(len(s1)):
                hashmap[s1[i]] = hashmap.get(s1[i], 0) + 1
                hashmap[s2[i]] = hashmap.get(s2[i], 0) - 1

            for v in hashmap.values():
                if v:
                    return False

            return True

        for i in range(len(strs)):
            if i in hashset:
                continue
            hashset.add(i)
            res.append([strs[i]])
            for j in range(i + 1, len(strs)):
                if j in hashset:
                    continue
                if isAnagram(strs[i], strs[j]):
                    hashset.add(j)
                    res[-1].append(strs[j])

        return res


        
