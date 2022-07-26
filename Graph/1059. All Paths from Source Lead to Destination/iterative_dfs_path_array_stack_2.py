class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # dfs iterative using stack - path included as argument in stack along with source

        # could not implement iterative dfs using 2 sets cycle and visited

        adj_list = {src: set() for src, dst in edges}
        for src, dst in edges:
            adj_list[src].add(dst)

        stack = [(source, [source])] # path to detect cycle
        while stack:
            vertex, path = stack.pop()

            if vertex not in adj_list:
                if vertex != destination:
                    return False
                else:
                    continue

            for node in adj_list[vertex]:
                if node in path: # cycle detected
                    return False
                stack.append((node, path + [node]))

        return True
