from typing import List

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def has_exactly_4_divisors(self, n: int) -> int:
        if n <= 5:
            return 0

        # case 1: n = p^3
        p = round(n**(1/3))
        if p**3 == n and self.is_prime(p):
            return 1 + p + p**2 + p**3

        # case 2.1: n = 2 * q
        if n % 2 == 0:
            q = n // 2
            if q != 2 and self.is_prime(q):
                return 1 + 2 + q + n
            return 0

        # case 2.2: n = p * q (odd)
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                j = n // i
                if i != j and self.is_prime(j):
                    return 1 + i + j + n
                return 0
        return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        n has exactly 4 divisors
        => n = 1 . p . q . n
        with p, q is prime and 1 < p < q < n
        or we can divide it into 2 cases:
        - case 1: n = p^3 with is_prime(p) -> n has 4 divisors: 1, p, p^2, p^3
        - case 2: n = p . q with p, q is_prime() and p != q (we can set that p < q)
        Time Complexity: O(sqrt(n)) because in Worst Case we loop from 2 to sqrt(n)
        """
        return sum(self.has_exactly_4_divisors(x) for x in nums)
