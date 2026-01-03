class Solution:
    def binaryGap(self, n: int) -> int:
        bits = []
        while n > 0:
            bits.append(n % 2)
            n //= 2
        print(bits)
        
        i = 0
        max = 0
        while i < len(bits):
            if bits[i] == 1:
                j = i
                i += 1
                while i < len(bits) and bits[i] == 0:
                    i += 1
                if i == len(bits):
                    return max
                if (i - j) > max:
                    max = i - j
            else:
                i += 1
                
        return max
                
