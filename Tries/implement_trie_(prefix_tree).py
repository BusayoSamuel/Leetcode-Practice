"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""

class MyTrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class MyTrie: #Time complexity O(n), Space complexity O(n^m) where n is the average size of a word and m is the number of words

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)