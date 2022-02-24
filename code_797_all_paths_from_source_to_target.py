class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def dfs(current_node, path):
            if current_node == len(graph) - 1:
                result.append(path)
            else:
                for node in graph[current_node]:
                    dfs(node, path + [node])
        
        result = []
        dfs(0, [0])

        return result