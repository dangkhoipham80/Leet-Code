class Solution:
    def largestEven(self, s: str) -> str:
        k = 0
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 0:
                k = i + 1
                break

        if k == 0:
            return ""
        
        return s[:k]