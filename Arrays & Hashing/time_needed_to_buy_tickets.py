"""
https://leetcode.com/problems/time-needed-to-buy-tickets/description/
"""

class MySolution: #Time complexity O(n*k) Space complexity O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i = 0
        while tickets[k]:
            i = 0 if i >= len(tickets) else i 
            if tickets[i]:
                res += 1
                tickets[i] -= 1
            i += 1

        return res

class CleanerSolution:  #Time complexity O(n) Space complexity O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else: 
                res += min(tickets[i], tickets[k] - 1)

        return res
