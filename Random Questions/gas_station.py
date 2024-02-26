"""
https://leetcode.com/problems/gas-station/description/
"""


class InefficientSolution: #Time complexity O(n^2), Space complexity O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def canStartAt(idx):
            tank = gas[idx] - cost[idx]
            i = idx + 1

            while i % len(gas) != idx:        
                if tank < 0:
                    return False
                tank += gas[i % len(gas)] - cost[i % len(gas)]
                i += 1

            return tank >= 0


        for i in range(len(gas)):
            if canStartAt(i):
                return i

        return -1


class BestSolution: #Time complexity O(n), Space complexity O(1)
    """
    [a, b, c] - gas
    [d, e, f] - cost
    Assume we met the key condition
    a + b + c >= d + e + f
    (a - d) + (b - e) + (c - f) >= 0
    If start at a-station and we reach end of the array and tank gas always non-negative then it's solution, obvious
    But other cases are more interesting
    if a - d < 0, then we could not start from it
    if b - e < 0, the same again
    Remains to prove that c-station is answer 100 %
    We know that (a - d) + (b - e) + (c - f) >= 0
    so it leads to
    (c-f) > 0 -> (c - f) + (a - d) > 0 -> (c - f) + (a - d) + (b - e) >= 0 so we really can travel around the circuit from that station as we always have non-negative gas tank.
    Hope, that could help someone. For me it was not so obvious.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost)) < 0:
            return - 1

        tank, start = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1

        return start