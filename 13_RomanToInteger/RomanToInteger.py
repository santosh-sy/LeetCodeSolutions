class Solution:
    def romanToInt(self, s: str) -> int:
        romanVals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        for i in range(len(s) - 1):
            if romanVals.get(s[i]) >= romanVals.get(s[i + 1]):
                result += romanVals.get(s[i])
            else:
                result -= romanVals.get(s[i])
        result += romanVals.get(s[-1])
        return result