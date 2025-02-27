# The code detects cycles in a directed graph (course prerequisites) using DFS and a visited set, 
# ensuring that no course depends on itself in a loop, allowing all courses to be completed.

# Time Complexity: O(V + E) (Each course (V) and its prerequisites (E) are visited once).
# Space Complexity: O(V + E) (Stores adjacency list preMap and recursive call stack in worst case).
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True