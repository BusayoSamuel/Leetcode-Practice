"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
"""

class TrieNode:
    def __init__(self):
        self.branches = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None: #Time complexity O(m)
        cur = self.head   
        for c in word:
            if c not in cur.branches:
                cur.branches[c] = TrieNode()
            cur = cur.branches[c]
        cur.word = True
        

    def search(self, word: str) -> bool: #Time complexity O((26^k)*m), Space complexity 0(n * m) where m is the average length of a word, n is the number of word and k is the number of wildcards
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for branch in cur.branches.values(): #We search every possible word with this prefix
                        if dfs(i+1, branch):
                            return True
                    return False #If none of them match, then we return false
                else:
                    if c not in cur.branches:
                        return False
                    cur = cur.branches[c]
            return cur.word #if we are at the last letter then it should have its word set to true
        return dfs(0, self.head) #so we start checking from the first letter
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
