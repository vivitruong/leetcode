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


#in Java
# class Solution {
#     //This would be easily solved by DFS and then comparing the values
#     public boolean dfs(TreeNode root, int targetSum, int currSum){
#         if(root == null) return false;

#         currSum += root.val;
#         if(root.left == null && root.right == null){
#             return (currSum == targetSum);
#         }
#         return dfs(root.left, targetSum, currSum) || dfs(root.right, targetSum, currSum);
#     }
#     public boolean hasPathSum(TreeNode root, int targetSum) {
#         return dfs(root, targetSum, 0);
#     }
# }


#in Javascript
# var hasPathSum = function(root, targetSum) {

#     const ans = [];
#     function goDFS(node, curruntSum) {

#     if(!node) return;

#         if(!node.left && !node.right) {
#             ans.push(node.val + curruntSum);
#         }

#         goDFS(node.left, curruntSum + node.val);
#         goDFS(node.right, curruntSum + node.val);
#     }
#     goDFS(root, 0);

#     return ans.includes(targetSum);
# };
