"""
https://leetcode.com/problems/implement-magic-dictionary/description/
"""

class MagicDictionary: 

    def __init__(self):
        self.dict = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary
        

    def search(self, searchWord: str) -> bool: #Time complexity O(nm) where n is the size of the dict and m is the length of searchWord, Space complexity O(1)
        def isTrue(s1, s2):
            idx1 = 0
            idx2 = 0
            count = 0
            while idx1 < len(s1):
                if s1[idx1] != s2[idx2]:
                    count += 1
                idx1 += 1
                idx2 += 1

            return count == 1



        for word in self.dict:
            if len(word) != len(searchWord):
                continue
                
            if isTrue(searchWord, word):
                return True

        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

class MagicDictionary:

    def __init__(self):
        self.myDict = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            self.myDict[n].add(word)

    def search(self, searchWord: str) -> bool: #slightly quicker, the use of hashmaps makes it easier to directly compare words of the same length
        n = len(searchWord)
        if n not in self.myDict: return False
        
        def diff(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1 
                if count > 1:
                    return count
            return count
                        
        
        for word in self.myDict[n]:
            if diff(word, searchWord) == 1:
                return True
        return False
