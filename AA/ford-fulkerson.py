def ford_fulkerson(possible_paths, graph):
    flow = 0
    # Sort possible paths based on the minimum edge value
    possible_paths.sort(key=lambda path: min(graph[path[i]][path[i + 1]] for i in range(len(path) - 1)))
    
    # Traversing each possible path one by one
    for path in possible_paths:
        min_edge = float('inf')
        # Finding the augmenting (minimum edge)
        for i in range(len(path) - 1):
            edge_length = graph[path[i]][path[i + 1]]
            min_edge = min(min_edge, edge_length)
        # Updating the capacities and handling bottlenecks (full flow)
        for i in range(len(path) - 1):
            # When edge in full flow
            if graph[path[i]][path[i + 1]] == 0:
                print(f'Path {path} not possible')
                break
            else:
                graph[path[i]][path[i + 1]] -= min_edge
        flow += min_edge
    return flow


# DFS approach to find all possible paths
def dfs_paths(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# graph = {
#     'S' : {'A' : 3, 'B' : 2},
#     'A': {'B': 5, 'T' : 2 },
#     'B': {'T': 3}
# }

# graph2 = {
#     'S' : {'A' : 100, 'B' : 100},
#     'A': {'C': 7},
#     'B': {'C': 3},
#     'C':{'T':1}
# }


# graph3 = {
#     'S' : {'A' : 9, 'D' : 3},
#     'A': {'B': 9},
#     'B': {'T': 2},
#     'D': {'C':4,'B':7},
#     'C':{'T':5}
# }

graph4 = {
    '1' : {'2' : 8, '3' : 10},
    '2': {'4': 2,'5':7},
    '3': {'2': 3,'5':12},
    '4': {'6':10},
    '5':{'4':4,'6':8}
}

source = '1'
target = '6'
possible_paths = dfs_paths(graph4, source, target)
print("All possible paths from", source, "to", target, ":", possible_paths)

max_flow = ford_fulkerson(possible_paths,graph4)
print('Max flow is : ',max_flow)