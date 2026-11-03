/*
https://leetcode.com/problems/implement-trie-prefix-tree/description/
*/

class TrieNode{
    constructor(){
        this.children = new Map()
        this.word = false
    }
}

class PrefixTree {
    constructor() {
        this.root = new TrieNode()
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let cur = this.root
        for(let c of word){
            if(!cur.children.has(c)){
                cur.children.set(c, new TrieNode())
            }
            cur = cur.children.get(c)
        }
        cur.word = true
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        let cur = this.root
        for(let c of word){
            if(!cur.children.has(c)){
                return false
            }
            cur = cur.children.get(c)
        }
        return cur.word === true
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        let cur = this.root
        for(let c of prefix){
            if(!cur.children.has(c)){
                return false
            }
            cur = cur.children.get(c)
        }
        return true
    }
}

class TrieNode {
    constructor() {
        this.children = {};   // plain object now
        this.word = false;
    }
}

class PrefixTree {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let cur = this.root;
        for (const c of word) {
            if (!(c in cur.children)) {       // has(c)
                cur.children[c] = new TrieNode();  // set(c, ...)
            }
            cur = cur.children[c];            // get(c)
        }
        cur.word = true;
    }

    search(word) {
        let cur = this.root;
        for (const c of word) {
            if (!(c in cur.children)) return false;
            cur = cur.children[c];
        }
        return cur.word;
    }

    startsWith(prefix) {
        let cur = this.root;
        for (const c of prefix) {
            if (!(c in cur.children)) return false;
            cur = cur.children[c];
        }
        return true;
    }
}
