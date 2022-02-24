from code_797_all_paths_from_source_to_target import Solution

def test_example_1():
    s = Solution()
    graph = [[1,2],[3],[3],[]]
    output = [[0,1,3],[0,2,3]]
    assert s.allPathsSourceTarget(graph) == output

def test_example_2():
    s = Solution()
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    output = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    assert s.allPathsSourceTarget(graph) == output