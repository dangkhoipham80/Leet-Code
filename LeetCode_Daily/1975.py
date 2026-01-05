from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total += abs_val
                min_abs = min(min_abs, abs_val)
                if val < 0:
                    negative_count += 1

        # If number of negatives is even → all can be flipped positive
        # If odd → one element must remain negative
        return total if negative_count % 2 == 0 else total - 2 * min_abs
            