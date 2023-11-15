"""
https://leetcode.com/problems/remove-k-digits/description/
"""

class Solution1: #Time complexity O(n), Space complexity O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)): #configuring a monotonically increasing stack
            while stack and k > 0 and num[i] < stack[-1]: #optimising for the lowest possible starting number
                stack.pop()
                k -= 1
            stack.append(num[i])

        stack = stack[:len(stack)-k] #in the event that k is still > 0, remove the last k digits

        while stack and stack[0] == "0": #in the event that there are leading zeros
            stack = stack[1:]

        res = "".join(stack)
        return res if res else "0"
    

class Solution: #Brute force attempt, Time complexity O(n^k), Space complexity O(n^k)
    def removeKdigits(self, num: str, k: int) -> str:
        sys.set_int_max_str_digits(10000)
        res = []

        def remove(num, k):
            if num == "":
                res.append(0)
                return

            if k == 0:
                res.append(num)
                return
            
            for i in range(len(str(num))):
                curNum = str(num)
                curNum = curNum[:i] + curNum[i+1:]
                if curNum == "":
                    res.append(0)
                    return
                remove(int(curNum), k-1)

        remove(num, k)
        res.sort()
        return str(res[0])