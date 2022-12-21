class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number)-1):
            if number[i] == digit and int(number[i]) < int(number[i+1]): return number[:i]+number[i+1:]
        rightmost = number.rfind(digit)
        return number[:rightmost]+number[rightmost+1:]