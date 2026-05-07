# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        q = deque([(root,root.val-1,0)])
        ans = 0

        while q:
            node,parent_val,length = q.popleft()

            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1
            
            ans = max(ans,length)

            if node.left:
                q.append((node.left,node.val,length))
            if node.right:
                q.append((node.right,node.val,length))

        return ans