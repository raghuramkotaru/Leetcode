# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            x = len(q)
            

            for i in range (len(q)):
                va = q.popleft()
                
                if va.left:
                    q.append(va.left)
                if va.right:
                    q.append(va.right)
                if x==1:
                    res.append(va.val)
                x -= 1
        return res


        