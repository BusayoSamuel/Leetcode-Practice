/*
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
*/

class TrieNode{
    constructor(){
        this.children = {}
        this.word = false
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode()
    }

    /**
     * @param {string} word
     * @return {void}
     * Time complexity O(n), Space complexity O(n)
     */
    addWord(word) {
        let cur = this.root
        for(const c of word){
            if(!(c in cur.children)){
                cur.children[c] = new TrieNode()       
            }
            cur = cur.children[c]
        }
        cur.word = true
    }

    /**
     * @param {string} word
     * @return {boolean}
     * Time complexity O(n * 26^k), Space complexity O(k) where k is the number of dots and n is the word length
     */
    search(word) {
        const dfs = (cur, i) => {
            for(let j = i; j < word.length; j++){
                let c = word[j]
                if(c === '.'){
                    for(const child of Object.values(cur.children)){
                        if(dfs(child, j + 1)){
                            return true
                        }
                    }
                    return false
                }else{
                    if(!(c in cur.children)){
                        return false
                    }
                    cur = cur.children[c]
                }
            }
            return cur.word
        }
        return dfs(this.root, 0)
    }
}
