# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        count = 0
        
        def dfs(node,ma):
            nonlocal count
            if not node:
                return
            ma = max(ma,node.val)
            if node.val >= ma:
                count+=1
            dfs(node.left,ma)
            dfs(node.right,ma)
            
        dfs(root,root.val)
        return count
