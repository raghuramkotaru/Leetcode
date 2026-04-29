class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root,0)])
        cols = defaultdict(list)
        mi,ma = 0, 0

        while q:
            node, va = q.popleft()
            mi,ma =min(mi,va), max(ma,va)
            cols[va].append(node.val)
            if node.left:
                q.append((node.left, va-1))
            if node.right:
                q.append((node.right, va+1))
        return [cols[c] for c in range(mi,ma+1)]
            
            


