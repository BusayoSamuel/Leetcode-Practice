"""
https://leetcode.com/problems/sender-with-largest-word-count/description/
"""

class MySolution: #Time complexity O(nm), Space complexity O(n) where n is the number of senders and m is the average number of messages
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hashmap = defaultdict(int)

        for i in range(len(messages)):
            count = len(messages[i].split(" "))
            hashmap[senders[i]] += count

        maxCount = 0
        res = ""

        for sender, count in hashmap.items():
            if count > maxCount:
                maxCount = count
                res = sender
            elif count == maxCount:
                res = max(res, sender)

        return res


from collections import defaultdict
from typing import List

class OptimisedSolution: #Time complexity O(nm), Space complexity O(n) where n is the number of senders and m is the average number of messages
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hashmap = defaultdict(int)

        for i in range(len(messages)):
            count = messages[i].count(" ") + 1  # Count words by counting spaces + 1
            hashmap[senders[i]] += count

        # Find the sender with the highest word count, ties broken by lexicographic order
        max_sender = max(hashmap.items(), key=lambda x: (x[1], x[0]))

        return max_sender[0]


            
