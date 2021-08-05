"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        l, r = [],[]
        root = l 
        def helper(root):
            lst = []
            while root:
                lst.append(root)
                root = root.parent
            return lst
        
        
        l = helper(p)
        r = helper(q)
        
        for i in range(len(l)):
            if l[i] in r:
                return l[i]
        return None