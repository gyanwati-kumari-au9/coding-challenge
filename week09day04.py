#Q.Write a graph construction + BFS traversal code

def addEdge(u,v,graph,undir = True):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

    if undir:

        if v not in graph:
            graph[v]=[]
        graph[v].append(u)

def addEdgeWithWeight(u,v,weit,graph,undirected = True):
    if u not in graph:
        graph[u] = []
    graph[u].append((v,weit))
    
    if undirected:
        if v not in graph:
            graph[v] = []
            graph[v].append((u,weit))

def addEdgeAdjMatrix(u,v,graph,undirected = True):
    graph[u][v] = 1
    if undirected:
        graph[v][u] = 1

def addEdgeAdjMatrixWeighted(u,v,weit,graph,undir = True):
    graph[u][v] = weit
    if undir:
        graph[v][u] = weit

def BFS(x):
    que = []
    visited = [False]*(len(graph))
    que.append(x)
    visited[x] = True
    while que:
        x = que.pop(0)
        print(x,end=' ')
        for i in graph[x]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True

if __name__=="__main__":
    graph = dict()
    # addEdge(1,2,graph,False)
    # graph = [[0 for x in range(5)] for x in range(5)]
    # addEdgeAdjMatrix(0,1,graph)
    # addEdgeAdjMatrix(0,2,graph)
    # addEdgeAdjMatrix(0,3,graph)
    # addEdgeAdjMatrix(0,4,graph)
    # print(graph)
    addEdge(0, 1,graph) 
    addEdge(0, 2,graph) 
    addEdge(1, 2,graph) 
    addEdge(2, 0,graph) 
    addEdge(2, 3,graph) 
    addEdge(3, 3,graph) 
  
    print ("Breadth First Traversal" "(starting from vertex 2)") 
    BFS(2) 
    