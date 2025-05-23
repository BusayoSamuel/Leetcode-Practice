'''
https://leetcode.com/problems/average-waiting-time/description/
'''

class MySolution: #Time complexity O(n), Space complexity O(1)
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = customers[0][0]
        total = 0

        for arrival, time in customers:
            if cur >= arrival:
                cur += time
            else:
                cur = arrival + time
                
            total += cur - arrival

        return total / len(customers)

class OtherSolution: #Same complexity
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0

        for arrival, order in customers:
            if t > arrival:
                total += t - arrival
            else:
                t = arrival
            total += order
            t += order

        return total / len(customers)
