class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def inner(node, targetSum):
            if not node.left and not node.right:
                return targetSum == node.val
            if node.left and inner(node.left, targetSum-node.val):
                return True
            if node.right and inner(node.right, targetSum-node.val):
                return True
            return False
        return inner(root, targetSum)
