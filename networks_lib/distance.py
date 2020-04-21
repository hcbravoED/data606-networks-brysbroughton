import numpy as np
from collections import deque

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (np.array): distance matrix
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
#Input: Adjacency matrix of size n by n  
#Output: Distance matrix `dist` of size n by n  
#    - For each vertex `u` in the network  
#    - Create boolean array `visited` of length n   
#    - Initialize all vertices u as `visited[u]=False`  
#    - Push tuple `(u, 0)` to a (first-in-first-out) queue `Q`  
#    - While `Q` is not empty:  
#        - Pop tuple `(v,d)` from the top of `Q`  
#        - Set `visited[v]=True`  
#        - Set distance `dist[u,v]=d`  
#        - For each neighbor `w` of `v`  
#            - if `visited[w]=False`, push tuple `(w, d+1)` to `Q`  


def bfs_distance(mat):
    num_vertices = mat.shape[0]    
    res = np.full((num_vertices, num_vertices), np.inf)
    
    
    #import pdb
    #from pdb import set_trace as bp
    #bp()
    
    # Finish this loop
    for u in range(num_vertices):
        #print("u: %d" % u)
        visited = np.full((num_vertices), False)
        crawl_queue = deque()
        crawl_queue.append((u, 0))

        while(len(crawl_queue) > 0):
            node = crawl_queue.popleft()
            visited[node[0]] = True
            if node[1] < res[u, node[0]]:
                res[u, node[0]] = node[1] 
            if node[1] < res[node[0], u]:
                res[node[0], u] = node[1]
            #print(np.where(mat[node[0]] == 1)[0])
            for w in np.where(mat[node[0]] == 1)[0]:
                #print(w)
                if not visited[w]:
                    #print('not visited')
                    crawl_queue.append((w, node[1] + 1))
                    #print(crawl_queue)
        
    return res

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (list of np.array): list of components
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
#The procedure will roughly be:

#- mark all vertices are `unused`
#- while any nodes are `unused`:
#  - choose any unused node `u`
#  - return `u` and all vertices `v` with `d(u,v) < np.inf` as a component and mark as used.

def get_components(mat):
    dist_mat = bfs_distance(mat)
    num_vertices = mat.shape[0]
    available = [True for _ in range(num_vertices)]

    components = [[]]
    
    #import pdb
    #from pdb import set_trace as bp
    #bp()
    
    # finish this loop
    while any(available):
        node = available.index(True)
        components[-1].append(node)
        available[node] = False
        
        #Must BFS to find components
        node_neighbors = np.where(mat[node] == 1)[0]
        crawl_queue = deque(node_neighbors)
        
        while(len(crawl_queue) > 0):
            n = crawl_queue.popleft()
            if available[n]:
                components[-1].append(n)
                available[n] = False
                for nn in np.where(mat[n] == 1)[0]:
                    crawl_queue.append(nn)
            else:
                components.append([])
                break
        
    
    # this is for testing purposes remove from final solution
    #components = [np.arange(num_vertices)]
    
    if len(components[-1]) == 0:
        components.pop()
    
    return components
