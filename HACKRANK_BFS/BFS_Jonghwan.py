def findShortestPath(graph,s):
    visited = set()
    queue = []
    distance = [-1 for x in range(len(graph))]
    distance[s] = 0
    predecessor = s
    queue.append(s)
    while queue:
        u = queue.pop(0)
        #print(u)
        #print(graph[u])
        adjcent_nodes = [x for x in range(len(graph)) if graph[u][x] != -1 and graph[u][x] != 0 and not x in visited]
        #print(adjcent_nodes)
        for adjcent_node in adjcent_nodes:
            if not adjcent_node in visited:
                visited.add(adjcent_node)
                distance[adjcent_node] = distance[predecessor] + 6
                predecessor = u
                queue.append(adjcent_node)
    #print(distance)
    res = [distance[x] for x in range(len(distance)) if x != s and x != 0 ]
    for x in res:
        print(x, end = ' ')
    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    #graph = Graph(n)
    graph = [[-1 for x in range(n+1)] for y in range(n+1)]
    for n in range(n):
        graph[n][n] = 0
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph[y][x] = 6
        graph[x][y] = 6
        #graph.connect(x-1,y-1) 
    #print(graph)
    s = int(input())
    findShortestPath(graph,s)
    print()
    
