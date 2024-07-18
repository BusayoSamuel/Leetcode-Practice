"""
https://leetcode.com/problems/reorganize-string/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        minheap = [[-count, value] for value, count in counts.items()]
        heapq.heapify(minheap)
        res = []

        for _ in range(len(s)):
            count, value = heapq.heappop(minheap)

            if res and value == res[-1]:
                if minheap:
                    temp = [count, value]
                    count, value = heapq.heappop(minheap)
                    heapq.heappush(minheap, temp)
                else:
                    break


            res.append(value)

            count += 1

            if count:
                heapq.heappush(minheap, [count, value])

        return "".join(res) if len(res) == len(s) else ""

class PerhapsCleanerSolution: #Same complexity
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # Hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # O(n)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res


class DefinitelyCleanerSolution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxheap = [[-count, value] for value, count in counts.items()]
        heapq.heapify(maxheap)
        res = []
        
        prev_count, prev_char = 0, ""
        
        while maxheap:
            count, char = heapq.heappop(maxheap)
            res.append(char)
            
            # Put the previous character back into the heap if it still has a count left
            if prev_count < 0:
                heapq.heappush(maxheap, [prev_count, prev_char])
            
            # Update the previous character and its count
            prev_count, prev_char = count + 1, char
        
        return "".join(res) if len(res) == len(s) else ""


        
