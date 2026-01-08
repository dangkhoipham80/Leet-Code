from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Key constraint:
        The subsequences must be non-empty:
        If all possible nums1[i] * nums2[j] are negative, are we allowed to return 0? -> nope, we must be return
        maximum dot product it can be created even when it's negative


        To approach, we supposed that 500 >= len(nums1) >= len(nums2) >= 1
        1. Base case:
        len(nums2) == 1 -> suppose len(nums2) == 1
        if nums2[0] >  0 -> choose max(nums1)
                    == 0 -> choose any in nums1
                    <  0 -> choose min(nums1)
        => Do we actually need to hard-code this base case? -> of course no

        if nums1 or nums2 only contains 0 -> return 0
        """
        m, n = len(nums1), len(nums2)

        dp = [[float("-inf")] * (m + 1) for _ in range(n + 1)]
        """
        dp =
            [
            [-∞, -∞, -∞, ..., -∞],   # row 0 (length m+1)
            [-∞, -∞, -∞, ..., -∞],   # row 1
            ...
            [-∞, -∞, -∞, ..., -∞]    # row n
            ]
        """

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                prod = nums1[i] * nums2[j]

                # skip nums[i]
                option1 = dp[i + 1][j]

                # skip nums[j]
                option2 = dp[i][j + 1]

                # pair (i, j) or skip both
                prod_next = dp[i + 1][j + 1]
                option3 = max(prod + prod_next, prod)

                dp[i][j] = max(option1, option2, option3)


        return dp[0][0]