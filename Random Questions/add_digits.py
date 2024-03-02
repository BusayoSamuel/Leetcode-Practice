"""
https://leetcode.com/problems/add-digits/description/
"""

class TrivialSolution: #Time complexity O(n), Space complexity O(1)
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) > 1:
            res = 0
            for c in str(num):
                res += int(c)
            num = res

        return num


class CrazySolution: #Time complexity O(1), Space complexity O(1)
    """
    We can find regular pattern by enumerate following case:
    1=1; 2=2; 3=3; 4=4; 5=5; 6=6; 7=7; 8=8; 9=9;
    10=1; 11=2; 12=3; 13=4; 14=5; 15=6; 16=7; 17=8; 18=9;
    19=1; 20=2; 21=3; 22=4; 23=5; 24=6; 25=7; 26=8; 27=9;

    so we see easily solve using %9 although multiples of 9 would return 0
    """
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 9 if num % 9 == 0 else num % 9