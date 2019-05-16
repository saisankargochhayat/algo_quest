# #Adjacency Matrix implementation by using dictionary
# n=int(input())
# edges = [('a', 'b'), ('a', 'd'), ('a', 'c'),('a','e')]
# from collections import defaultdict
#
# matrix = defaultdict(int)
# for edge in edges:
#     matrix[edge] += 1
#
# print(matrix)
#
# #Adjacency matrix using dictionary and groupby
# from itertools import groupby
#
# edges = [(1, 2), (2, 3), (1, 3)]
#
# adj = {k: [v[1] for v in g] for k, g in groupby(sorted(edges), lambda e: e[0])}
# # adj: {1: [2, 3], 2: [3]}
#https://algocoding.wordpress.com/2014/08/25/form-the-adjacency-matrix-and-adjacency-lists-from-the-edges/
n=int(input())
e=int(input())
edge_u=list()
edge_v=list()
adjMatrix = [[0 for i in range(n)] for k in range(n)]
for i in range(e):
    m,n=map(int,input().split())
    edge_u.append(m)
    edge_v.append(n)
#populate matrix
for i in range(len(edge_u)):
        u = edge_u[i]
        v = edge_v[i]
        adjMatrix[u][v] = 1

print("Adjacency matrix: ")
print(adjMatrix)
#bettr print
# def printMatrix(matrix):
#     for i in range(len(matrix)):
#         for k in range(len(matrix[0])):
#             print(matrix[i][k], " ", end='')
#         print('')
