import math

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @classmethod
    def maxDepth(cls, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        return Solution.find_depth(root, 1)
    
    @classmethod
    def find_depth(cls, root: TreeNode, current_depth: int) -> int:


        left_depth = current_depth  if root.left is None else Solution.find_depth(
                root.left, current_depth+1)

        right_depth = current_depth  if root.right is None else Solution.find_depth(
                root.right, current_depth+1)

        print("I'm on {}, left_depth = {}, right_depth = {}".format(root.val, left_depth, right_depth))
        return left_depth if left_depth > right_depth else right_depth

class Input:
    
    @classmethod
    def parse_tree(cls, values: list) -> TreeNode:
        """Returns the root of a binary tree encoding the input values.

        Args:
            values (list): input values starting with the top one, then going through its children, left-to-right

        Returns:
            TreeNode: a binary tree root
        """
        
        values = [3,9,20,"null","null",15,7]
        

