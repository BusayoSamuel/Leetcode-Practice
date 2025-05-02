"""
https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
"""

class MyBruteSolution: #Inefficient, Time complexity 0(nm), Space complexity O(n)
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for q in queries:
            count = 0
            for w in range(q[0], q[1]+1):
                if words[w][0] in vowels and words[w][-1] in vowels:
                    count += 1
            res.append(count)

        return res
        

class MySolution: #Time complexity O(n), Space complexity O(n)
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0]
        count = 0

        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                count += 1
            prefix.append(count)

        print(prefix)
                 
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            res[i] = prefix[q[1]+1] - prefix[q[0]]

        return res


class OtherSolution: #Same complexity as above
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set("aeiou")
        prefix_cnt = [0] * (len(words) + 1)
        prev = 0

        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1
            prefix_cnt[i + 1] = prev

        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_cnt[r + 1] - prefix_cnt[l]

        return res
