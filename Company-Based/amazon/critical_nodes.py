# https://codeforces.com/blog/entry/71146
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/504797/Python-Find-bridgesarticulation-points-with-detailed-explanation

from collections import defaultdict
def find_articulation_points(nodeNum, edges):
    # Build the graph first 
    def APUtil(u, visited, ap, parent, low, disc,graph,time): 

        children =0

        # Mark the current node as visited and print it 
        visited[u]= True

        # Initialize discovery time and low value 
        disc[u] = time 
        low[u] = time 
        time += 1

        for v in graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                APUtil(v, visited, ap, parent, low, disc,graph,time) 

                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[v]) 

                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1:
                    ap.add(u)
                    

                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[v] >= disc[u]: 
                    ap.add(u)  
                    
                # Update low value of u for parent function calls     
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v]) 
        return 



    graph = defaultdict(list)
    for edge in  edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        

    visited = [False] * nodeNum 
    disc = [float("Inf")] * nodeNum 
    low = [float("Inf")] * nodeNum 
    parent = [-1] * nodeNum 
    ap = set() 
    time = 0

    # Call the recursive helper function 
    # to find articulation points 
    # in DFS tree rooted with vertex 'i' 
    for i in range(nodeNum ): 
        if visited[i] == False:
            APUtil(i, visited, ap, parent, low, disc,graph,time) 
    return list(ap)


print(find_articulation_points(7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))  
print(find_articulation_points(5, [[0, 1], [1, 2], [3, 1], [4, 1], [4, 3], [2, 0]]))  