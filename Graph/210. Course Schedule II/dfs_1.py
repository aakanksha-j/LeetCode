class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # neetcode solution

        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states
        # visited -> course has been added to output, no cycle detected
        # visiting -> course not added to output but added to cycle
        # unvisited -> course not added to output or cycle

        output = []
        visit, cycle = set(), set()
        def dfs(cr):
            if cr in cycle:
                return False
            if cr in visit:
                return True

            cycle.add(cr)
            for pre in prereq[cr]:
                if dfs(pre) == False:
                    return False
            cycle.remove(cr)
            visit.add(cr)
            output.append(cr)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output
