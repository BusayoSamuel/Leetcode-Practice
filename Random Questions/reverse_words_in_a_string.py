"""
https://leetcode.com/problems/reverse-words-in-a-string/description/
"""

class SimplestSolution: #Time complexity O(n), Space complexity O(n)
    def reverseWords(self, s: str) -> str:
        stack = s.split(" ")
        reverse = []

        for i in range(len(stack)-1, -1, -1):
            if stack[i] and stack[i] != " ":
                reverse.append(stack[i])

        return " ".join(reverse)
    
class MutableStringSolution: #Time complexity O(n), Space complexity O(n)
    def reverseWords(self, s: str) -> str:
        s = s.strip() # to get rid of trailing and leading spaces
        s = [*s] #To make string mutable
        l = 0
        r = len(s) - 1

        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r] , s[l]

                l += 1
                r -= 1

        reverse(l, r) #reverse the entire string

        for i in range(len(s)): #to delete extra spaces within
            if s[i] == " " and (i == 0 or s[i - 1] == " " or s[i-1] == "" or i == len(s)-1):
                s[i] = ""

        l = 0

        for r in range(len(s)): # to reverse each word
            if s[r] == " ":
                reverse(l, r-1)
                l = r + 1
        
        reverse(l, r)


        return "".join(s)
        