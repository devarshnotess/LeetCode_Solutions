# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        current = root
        while current:
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                temp.right = current.right
                current.right = current.left
                current.left = None
            current = current.right

        