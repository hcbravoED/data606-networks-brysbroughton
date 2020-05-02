import numpy as np
import random

## TODO: Implement this function
##
## Input:
##  - dmat (np.array): symmetric array of distances
##  - K (int): Number of clusters
##
## Output:
##   (np.array): initialize by choosing random number of points as medioids
def random_init(dmat, K):
    num_vertices = dmat.shape[0]
    vertices = [v for v in range(0, num_vertices)]
    medioids = []
    for k in range(K):
        choice = random.choice(vertices)
        medioids.append(choice)
        vertices.remove(choice)
    return medioids

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - medioids (np.array): indices of current medioids
##
## Output:
##   - (np.array): assignment of each point to nearest medioid
def assign(dmat, medioids):
    num_vertices = dmat.shape[0]
    ret = np.zeros((num_vertices))
    
    for i in range(len(medioids)):
        medioids[i] = int(medioids[i])
    
    print('assign', dmat, medioids)
    
    
    for v in range(num_vertices):
        distances = sorted([(dmat[v][m], m) for m in medioids])
        #print(distances)
        ret[v] = distances[0][1]
        #print(np.argmin(dmat[:,medioids], axis=1))
        #ret[v] = np.argmin(dmat[:,medioids], axis=1)
    
    print(ret)
    
    return ret

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - assignment (np.array): cluster assignment for each point
##   - K (int): number of clusters
##
## Output:
##   (np.array): indices of selected medioids
def get_medioids(dmat, assignment, K):
    mediods = np.zeros((K))
    
    print(dmat, assignment, K)
    
    #select for each assignment a new medioid that is the point
    #closest to all other points in that assignment
    ass = {} #{m1:[v1,v2,v5], m2:[v3,v4,v6]}
    for i in range(len(assignment)):
        #print(i, assignment[i])
        ass[assignment[i]] = [i] if not assignment[i] in ass else ass[assignment[i]] + [i]
    
    new_meds = []
    print('ass', ass)
    for med in ass:
        #[(distance to all other nodes in assignment, node number)]
        node_dists = {}
        for node in ass[med]:
            node_dists[node] = 0
            for other in ass[med]:
                node_dists[node] += dmat[node][other]
        #[(np.sum(np.where(dmat[node] in ass)), node) for node in ass[med]]
        print('dists', node_dists)
        new_med = min(node_dists, key=node_dists.get)
        #for node in ass[med]:
        #    mediods[node] = new_med
        new_meds.append(new_med)
    
    for i in range(K):
        mediods[i] = new_meds[i]
    
    print('ret get medioids', mediods, new_meds)
    
    #return mediods
    return new_meds

## TODO: Finish implementing this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - K (int): number of clusters
##   - niter (int): maximum number of iterations
##
## Output:
##   - (np.array): assignment of each point to cluster
def kmedioids(dmat, K, niter=10):
    num_vertices = dmat.shape[0]
    
    # we're checking for convergence by seeing if medioids
    # don't change so set some value to compare to
    old_mediods = np.full((K), np.inf, dtype=np.int)
    medioids = random_init(dmat, K)
    
    # this is here to define the variable before the loop
    assignment = np.full((num_vertices), np.inf)
   
    it = 0
    while np.any(old_mediods != medioids) and it < niter:
        it += 1
        old_medioids = medioids
        
        # finish implementing this section
        assignment = assign(dmat, medioids)
        medioids = get_medioids(dmat, assignment, K)
        #

    return assignment
        