# Approach:
# Perform a Breadth-First Search (BFS) using a queue, processing nodes level by level and storing values in a list.
# For each level, traverse all nodes, append their values, and enqueue their children for the next level.
# Time Complexity: O(n) (Each node is visited once).
# Space Complexity: O(n) (Queue stores at most one level of nodes at a time).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque(
            [
                root,
            ]
        )
        while queue:
            levels.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = level + 1
        return levels