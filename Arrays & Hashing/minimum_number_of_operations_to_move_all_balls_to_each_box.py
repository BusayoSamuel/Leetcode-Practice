"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
"""


class MySolution: #Time complexity: 0(n^2), Space complexity: O(n)
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1' and j != i:
                    answer[i] += abs(j - i)

        return answer
