class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)

# n = 1 -> 1 + 4 = 1 + 4 * 1
# n = 2 -> 5 + 8 = 1 + 4 * (1 + 2)
# n = 3 -> 13 + 12