"""
https://leetcode.com/problems/backspace-string-compare/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        curS = []
        curT = []

        for i in range(len(s)):
            if s[i] == "#":
                if curS:
                    curS.pop()
            else:
                curS.append(s[i])


        for j in range(len(t)):
            if t[j] == "#":
                if curT:
                    curT.pop()
            else:
                curT.append(t[j])

        curS = "".join(curS)
        curT = "".join(curT)

        return curS == curT
        

class MySolution2: #Time complexity O(n), Space complexity O(n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        l = -1
        s = [*s]
        t = [*t]

        for r in range(len(s)):
            if s[r] == "#":
                if l >= 0:
                    l -= 1
            else:
                s[l+1], s[r] = s[r], s[l+1]
                l += 1

        s = "".join(s)
        s = s[:l+1]

        l = -1

        for r in range(len(t)):
            if t[r] == "#":
                if l >= 0:
                    l -= 1
            else:
                t[l+1], t[r] = t[r], t[l+1]
                l += 1

        t = "".join(t)
        t = t[:l+1]
        
        return s == t

class MoreEffecientSolution: #Time complexity O(n), Space complexity O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(string, index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and string[index] != "#":
                    break
                elif string[index] == "#":
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1

            return index

        index_s, index_t = len(s) - 1, len(t) - 1

        while index_s >= 0 or index_t >= 0:
            index_s = nextValidChar(s, index_s)
            index_t = nextValidChar(t, index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1

        return True

             
        
