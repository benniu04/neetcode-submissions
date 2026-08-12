# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Store value -> index mappings for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track our current position in preorder using an iterator or index pointer
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: valid inorder range is empty
            if in_left > in_right:
                return None
            
            # Pick current root value from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find root's position in inorder array in O(1) time
            mid = inorder_map[root_val]
            
            # Build left and right subtrees by restricting index boundaries
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
        
        return helper(0, len(inorder) - 1)