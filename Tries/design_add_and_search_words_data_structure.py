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


class MyTrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class MyWordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def helper(word, cur):
            for i in range(len(word)):
                c = word[i]
                if c != "." and c not in cur.children:
                    return False
                elif c == ".":
                    for child, node in cur.children.items():
                        if helper(word[i+1:], node):
                            return True
                    return False
                else:
                    cur = cur.children[c]
            return cur.word

        return helper(word, self.root)


class MyTrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class MyWordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def searchRoot(word, root):
            curr = root
            for i, c in enumerate(word):
                if c not in curr.children:
                    if c == '.':
                        for char in curr.children:
                            if searchRoot(word[i+1:], curr.children[char]):
                                return True
                    return False
                curr = curr.children[c]
            return curr.word

        return searchRoot(word, self.root)

