# 1161. Maximum Level Sum of a Binary Tree
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Understand problem:
        - Calculate the sum of values at each level of a binary tree.
        - Compare these sums:
        - Return the level (1-indexed) with the maximum sum. If multiple levels have the same sum, return the smallest level number.

        Examples:
        - Input: root = [1,7,0,7,-8,null,null]
          Output: 2
          Explanation:
          Level 1 sum = 1
          Level 2 sum = 7 + 0 = 7
          Level 3 sum = 7 + (-8) = -1
          The maximum sum is at level 2.

        Edge Cases:
        - The max sum can be negative if all node values are negative -> do not init sum = 0 => sum = float('-inf')

        Approach 1:
        - Use BFS to traverse the tree level by level.
        - Maintain a queue to keep track of nodes at the current level.
        - Add their children to the queue for the next level.
        """
        max_sum_level, max_smallest_level, curr_level = float("-inf"), 0, 0

        current_list_nodes = deque()
        current_list_nodes.append(root)

        while current_list_nodes:
            curr_level += 1
            sum_at_curr_level = 0

            len_curr_level = len(current_list_nodes)
            for _ in range(len_curr_level):
                node = current_list_nodes.popleft()
                sum_at_curr_level += node.val

                if node.left:
                    current_list_nodes.append(node.left)
                if node.right:
                    current_list_nodes.append(node.right)

            if max_sum_level < sum_at_curr_level:
                max_sum_level, max_smallest_level = sum_at_curr_level, curr_level

        return max_smallest_level
