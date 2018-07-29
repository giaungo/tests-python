

def find_optimal_path(edges, origin_vertex, weights):
    """
    Find a path such that the sum of the weights of all vertices on the path is maximized
    :param edges: array of edges
    :param origin_vertex: name of origin vertex
    :param weights: array of weights
    :return: max total of weights
    """
    graph = build_graph_from_edges(edges)
    vertices = list(weights.keys())
    paths = []
    for vertex in vertices:
        paths += find_all_paths(graph, origin_vertex, vertex)

    sum_of_weights = []
    for path in paths:
        sum_of_weights.append(sum([weights[ver] for ver in path]))

    return max(sum_of_weights)


def find_all_paths(graph, start, end, path=[]):
    """
    Finding all paths of graph
    :param graph: a graph as dictionary
    :param start: name of start vertex
    :param end: name of end vertex
    :param path: array of paths
    :return: list of all of paths
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def build_graph_from_edges(edges):
    """
    Build graph from edges
    :param edges: array of edges, for example [['A', 'B'], ['B', 'C'], ['A', 'C']]
    :return: graph as a dict of vertices, for example {'A': ['B', 'C'], 'B': ['C']}
    """
    graph = {}
    for edge in edges:
        start = edge[0]
        end = edge[1]
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    return graph
