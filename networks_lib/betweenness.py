import numpy as np

## TODO: Implement this function
##
## Implements the breadth-first algorithm of Girvan-Newman to compute
##   number (fractional) of shortest paths starting from a given vertex
##   that go through each edge of the graph
##
## Input:
##   - vertex (int): index of vertex paths start from
##   - mat (np.array): n-by-n adjacency matrix
##
## Output:
##   (np.array): n-by-n edge count matrix
##
## Note: assume input adjacency matrix is binary and symmetric
def edge_counts(vertex, mat):
    num_vertices = mat.shape[0]
    res = np.zeros((num_vertices, num_vertices))
    
    #list of all paths followed. path is a list of the nodes in order
    paths = [[vertex]]
    
    #import pdb
    #from pdb import set_trace as bp
    #bp()
    
    def rec_edge_count(level_count, prev_level, cur_level):
        if len(cur_level) == 0:
            return
        
        for u in prev_level:
            for v in cur_level:
                if mat[u][v] == 1:
                    for path in paths:
                        if path[-1] == u:
                            new_path = path + [v]
                            paths.append(new_path)
        for v in cur_level:
            for path in paths:
                if path[-1] == v:
                    length = len(path)
                    for i in range(0, length):
                        if i == length - 1:
                            break
                        res[path[i]][path[i+1]] += 1
                        res[path[i+1]][path[i]] += 1
                    
        #print(level_count, prev_level, cur_level, paths, res)
        
        current_neighbors = set([])
        for node in cur_level:
            current_neighbors = current_neighbors.union(np.where(mat[node] == 1)[0])
        
        #current_neighbors = list(set(current_neighbors))
        
        next_level = []
        
        for n in current_neighbors:
            if n in prev_level:
                continue
            if n in cur_level:
                continue
            if n in next_level:
                continue
            next_level.append(n)
            
        rec_edge_count(level_count + 1, cur_level, next_level)
    
    level1 = np.where(mat[vertex] == 1)[0]
    rec_edge_count(1, [vertex], level1)
    
    return res

## Compute edge betweeness for a graph
## 
## Input: 
##   - mat (np.array): n-by-n adjacency matrix. 
##
## Output:
##   (np.array): n-by-n matrix of edge betweenness
##
## Notes: Input matrix is assumed binary and symmetric
def edge_betweenness(mat):
    res = np.zeros(mat.shape)
    num_vertices = mat.shape[0]
    for i in range(num_vertices):
        res += edge_counts(i, mat)
    return res / 2.