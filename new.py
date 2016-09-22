# edgelist_to_adjlist.py

def printAdjList(adjList):
    for i in range(len(adjList)):
        print(i, ":", adjList[i])

#----------------------------------------------------------------

def main():

    edge_u = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4]
    edge_v = [1, 3, 4, 0, 2, 3, 4, 1, 3, 0, 1, 2, 4, 0, 1, 3]


    # our graph has n=5 nodes
    n = 5

    # create empty adjacency lists - one for each node -
    # with a Python list comprehension
    adjList = [[] for k in range(n)]
    print(adjList)


    # scan the arrays edge_u and edge_v
    for i in range(len(edge_u)):
        u = edge_u[i]
        v = edge_v[i]
        adjList[u].append(v)


    # check adjacency list
    print("Adjacency list: ")
    printAdjList(adjList)

#------------------------------------------------------------------

main()
