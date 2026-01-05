from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        4 3 2    1  -1
        3 2 1    -1  -1
        1 1 1    -2  -2
        1 -1 -2 -3   -3
        1 -1 -2  -3  -3
        """
        cnt = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    cnt += len(grid[0]) - c
                    break

        return cnt