# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root):
            if not root: return 
            if root.val == val:
                return root            
            return dfs(root.right) if val > root.val else dfs(root.left)
   
        return dfs(root)