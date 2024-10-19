"""
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/
"""

class Solution: #Time complexity O(n*m) where n is the len(words) and m is the size of the largest word, Space complexity O(1) because there's a finite number of possible characters (26)
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = defaultdict(int) #[char: count]

        for word in words:
            for c in word:
                hashmap[c] += 1

        n = len(words)
        for count in hashmap.values():
            if count < n or count % n != 0:
                return False

        return True

class Solution: #Same complexity
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = defaultdict(int) #[char: count]

        for word in words:
            for c in word:
                hashmap[c] += 1

        n = len(words)
        for count in hashmap.values():
            if count % n: #alternatively
                return False

        return True
