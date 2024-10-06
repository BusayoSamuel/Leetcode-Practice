"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def minOperations(self, s: str) -> int:
        op1 = "0"
        op2 = "1"

        while len(op1) < len(s):
            op1 += "1" if op1[-1] == "0" else "0"
            op2 += "1" if op1[-1] == "0" else "0"

        i = 0
        count1 = 0
        count2 = 0

        while i < len(s):
            if s[i] != op1[i]: count1 += 1
            if s[i] != op2[i]: count2 += 1

            i += 1

        return min(count1, count2)
    

class OptimalSolution: #Time complexity 0(n), Space complexity O(1)
    def minOperations(self, s: str) -> int:
        flag = 0 #a single flag is used to count for strings starting with 0
        zeroStartCount = 0

        for c in s:
            if int(c) != flag:
                zeroStartCount += 1

            flag = not flag

        oneStartCount = len(s) - zeroStartCount #counts for strings starting with one + counts for strings starting with zero = length of s

        return min(zeroStartCount, oneStartCount)


class MyOtherSolution: #Same complexity
    def minOperations(self, s: str) -> int:
        start1 = "0"
        start0 = "1"
        count0 = 0
        count1 = 0

        for c in s:
            if c == start1:
                count0 += 1
            else:
                count1 += 1

            start0, start1 = start1, start0

        return min(count0, count1)
