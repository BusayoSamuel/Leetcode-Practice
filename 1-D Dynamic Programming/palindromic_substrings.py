"""
https://leetcode.com/problems/palindromic-substrings/description/
"""

class MySolution: #Time complexity O(n^3), Space complexity O(n^2)
    def countSubstrings(self, s: str) -> int:
        count = 0
        cache = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]

                if sub in cache:
                    count += 1 if cache[sub] else 0
                    continue

                l = i
                r = j

                while l <= r:
                    if s[l] != s[r]:
                        cache[sub] = False
                        break

                    l += 1
                    r -= 1
                    
                    if l > r:
                        cache[sub] = True
                        count += 1

        return count


class EfficientSolution: #Time complexity O(n^2), Space complexity O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res


        
