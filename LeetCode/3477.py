# 3477. Fruits Into Baskets II
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0

        for f in fruits:
            i = 0
            while i < len(baskets):
                if f <= baskets[i]:
                    cnt += 1
                    baskets[i] = -1
                    break
                else:
                    i += 1

            # if i == len(baskets):
            #     return len(fruits) - cnt

        return len(fruits) - cnt

# Assert Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.numOfUnplacedFruits([1,2,3,4], [2,3]) == 2
    assert sol.numOfUnplacedFruits([1,2,3], [1,1,1]) == 2
    assert sol.numOfUnplacedFruits([5,4,3,2,1], [3,3,3]) == 2
    assert sol.numOfUnplacedFruits([1,2,2,3,4], [2,3,4]) == 2
    assert sol.numOfUnplacedFruits([1,1,1,1], [1,1]) == 2

    print("All tests passed!")