class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # bfs topological sort
        # https://leetcode.com/problems/parallel-courses/discuss/344807/Python-3-Topological-sorting
        # leetcode solution without using deque
        
        # time O(N+E)
        # space O(N+E)
        
        # testcase: 6 [[1,2],[2,5],[2,4],[3,4],[5,6],[4,6]]
        
        
        in_degree = {i: set() for i in range(1, n+1)}
        out_degree = {i: set() for i in range(1, n+1)}
        
        for pre, nxt in relations:
            in_degree[nxt].add(pre)
            out_degree[pre].add(nxt)
        
        queue = []
        for course in in_degree:
            if not in_degree[course]:
                queue.append((course, 1))
        
        course_completed = 0
        max_level = 0
        while queue:
            next_queue = []
            for node, level in queue: # course 1 = node
                course_completed += 1
                max_level = max(level, max_level)
                for edge in out_degree[node]: # course 2 = edge, we are checking all the edges of node
                    in_degree[edge].remove(node) # remove node from edges
                    if not in_degree[edge]: # if no prerequisite remaining for this edge, then we can take this course in next sem
                        next_queue.append((edge, level + 1))
            queue = next_queue
            
        return max_level if course_completed == n else -1
        
    