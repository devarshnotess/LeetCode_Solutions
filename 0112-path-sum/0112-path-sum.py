
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        sum = 0
        return self.dfs(root, targetSum, sum)

    def dfs(self, root, targetSum, sum):
        
        if root == None:
            return False

        sum += root.val

        if root.left == None and root.right == None:
            return sum == targetSum

        if self.dfs(root.left, targetSum, sum):
            return True
        if self.dfs(root.right, targetSum, sum):
            return True

        return False
        