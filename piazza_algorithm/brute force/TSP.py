graph = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 2, 3, 2, 3], # 정점 1
    [0, 2, 0, 3, 4, 1], # 정점 2
    [0, 3, 3, 0, 2, 4], # 정점 3
    [0, 2, 4, 2, 0, 5], # 정점 4
    [0, 3, 1, 4, 5, 0]  # 정점 5
]
START_NODE = 1

def tsp(graph):
    visited = [False] * len(graph)
    dfs(graph, START_NODE, visited, visited_count=0, cost=0)
    return

def dfs(graph, cur, visited, visited_count, cost):
    if visited_count == len(graph): # 모든 도시 방문
        if graph[cur][START_NODE] > 0: # dfs 경로가 헤밍턴 순회인 경우
            min_cost = min(min_cost, cost)
        return # dfs 종료
    
    N = len(graph)
    for next in range(N):
        if not visited[next] and graph[cur][next] > 0:
            visited[next] = True
            dfs(graph, next, visited, visited_count+1, cost + graph[cur][next]) # 다음 도시 방문
            visited[next] = False # dfs 종료 후 백트래킹
  
tsp(graph)

'''      
def _dfs(graph, start, visited, result):
    result.append(start)
    visited[start] = True
    for next in range(len(graph[start])):
        if graph[start][next] != 0 and not visited[next]:
            dfs(graph, next, visited, result)
    return result
'''