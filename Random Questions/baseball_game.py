"""
https://leetcode.com/problems/baseball-game/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(1)
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))


        return sum(record)
