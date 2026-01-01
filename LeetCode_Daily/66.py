from typing import List

# Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        nums = 123456789 => digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums = 0 => return 1 => digits = [1]
        nums = 999 => return 1000 => digits = [1, 0, 0, 0]
        nums = 129 => return 130 => digits = [1, 3, 0]
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        tmp = 1
        for i in range(len(digits) - 1, -1, -1):
            x = digits[i] + tmp
            if x < 10:
                digits[i] = x
                return digits
            else:
                digits[i] = 0
                tmp = 1

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

# Assert Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([9]) == [1, 0]
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert sol.plusOne([1, 9, 9]) == [2, 0, 0]
    assert sol.plusOne([0]) == [1]

    print("All tests passed!")