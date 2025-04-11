"""
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
"""

class MySolution:
  """
  Time complexity O(n) as we go through the entire string s in the worst case
  Space complexity O(1) as no extra space is used.
  """
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0

        while i < len(s):
            if s[i] == t[j]:
                j += 1

                if j == len(t):
                    return 0

            i += 1

        return len(t) - j
        
