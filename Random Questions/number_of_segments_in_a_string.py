"""
https://leetcode.com/problems/number-of-segments-in-a-string/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def countSegments(self, s: str) -> int:
        cur = ""
        s += " "
        count = 0
        for c in s:
            if c == " " and cur:
                count += 1
                cur = ""
                
            if c != " ":
                cur += c

        return count


class OtherSolution:
    def countSegments(self, s: str) -> int:
        n=len(s)
        c=0
        i=0
        while(i<n):
            while(i<n and s[i]==' '):i+=1
            count=False
            while(i<n and s[i]!=' '):
                i+=1
                count=True
            if(count):c+=1 
            i+=1  
        return c

class OtherSolution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

                
        
            
