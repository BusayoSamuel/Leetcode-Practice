"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
"""
class Solution: #Time complexity O(n), Space complexity O(n)
    def minFlips(self, s: str) -> int:
        s1 = "0"
        s2 = "1"
        n = len(s)
        s = s + s #string is doubled to consider every type-1 operation
        for i in range(len(s) - 1): #creating two alternating binary string, could be 01010... or 101010....
            s1 += "1" if s1[-1] == "0" else "0"
            s2 += "0" if s2[-1] == "1" else "1"

        res = float("Inf")
        l = 0
        r = 0
        count1 = 0
        count2 = 0
        sample = s

        while r < n: #consider the first case where no type-1 operation is used
            if r - l < n:
                if sample[r] != s1[r]:
                    count1 += 1
                if sample[r] != s2[r]:
                    count2 += 1
                r += 1
        res = min(res, min(count1, count2)) 

        while r < len(s): #consider every possible type-1 operation and update the minimum count
            if sample[l] != s1[l]:
                count1 -= 1
            if sample[l] != s2[l]:
                count2 -= 1
            l += 1
            if sample[r] != s1[r]:
                count1 += 1
            if sample[r] != s2[r]:
                count2 += 1
            r += 1
            res = min(res, min(count1, count2))

        return res


class MySolution: #Same complexity as above
    def minFlips(self, s: str) -> int:
        n = len(s)
        zero = '0'
        one = '1'
        alt1 = ''
        alt2 = ''
        s += s
        res = math.inf
        

        for i in range(len(s)):
            alt1 += one if i % 2 else zero
            alt2 += zero if i % 2 else one

        count1 = 0
        count2 = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] != alt1[r]:
                count1 += 1
            if s[r] != alt2[r]:
                count2 += 1


            if r-l+1 == n:
                res = min(res, count1, count2)

                if s[l] != alt1[l]:
                    count1 -= 1

                if s[l] != alt2[l]:
                    count2 -= 1

                l += 1
                

            
            r += 1


        return res


        


        
        
        
