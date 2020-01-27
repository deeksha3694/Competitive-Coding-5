import collections
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        q = collections.deque([root])
        while q:
            maxi = float('-inf')
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                maxi = max(curr.val, maxi)
                if curr.left :
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(maxi)
        return res