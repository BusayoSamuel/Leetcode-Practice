"""
https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description/
"""

class NotTheCleanestSolution: #Time complexity O(nlogn), Space complexity O(n)
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        sectVisit = [[i + 1, 0] for i in range(n)]
        cur = rounds[0]

        def loop(end):
            nonlocal cur
            while cur % n - 1 != end:
                sectVisit[cur % (n) - 1][1] += 1
                cur += 1
            sectVisit[cur % (n) - 1][1] += 1
            cur += 1
            

        for i in range(1, len(rounds)):
            loop(rounds[i] % n - 1)

        sectVisit.sort(key = lambda x: x[1], reverse = True)
        res = []
        
        for i in range(len(sectVisit)):
            if res and (i > 0 and sectVisit[i][1] != sectVisit[i-1][1]):
                break

            res.append(sectVisit[i][0])

        res.sort()

        return res


class BetterSolution: #Time complexity O(n), Space complexity O(1)
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1] #It only matters what the first and last values are because it goes in a loop

        if first <= last:
            return list(range(first, last+1))
        else:
            return list(range(1, last + 1)) + list(range(first, n+1))
