# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-revisited-9e1091ea/
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
import sys
from heapq import heapify, heappush, heappop ,heappushpop
 
def rl():
    return sys.stdin.readline()
    
def findShortestPath(N,M,K,graph):
    INT_MAX = 1000000000
    dp = [[INT_MAX for _ in range(K+1)] for _ in range(N+1)]
    #vis = [False]*(N+1)
    
    dp[1] = [0]*(K+1)
    pQueue = []
    #Min Weight, node, parent
    heappush(pQueue,(0,1,0))
    
    while pQueue:
        temp = heappop(pQueue)
        node = temp[1]
        parent = temp[2]
        
        for next_node,w in graph[node]:
            if next_node != parent:
                      
                flag = False
                for i in range(K+1):
                    
                    if(i==0 and (dp[next_node][i] > (dp[node][i]+w))):
                        dp[next_node][i] = min(dp[next_node][i],dp[node][i]+w)
                        flag = True
                        
                    elif i!=0 and dp[next_node][i]> dp[node][i-1] or dp[next_node][i]>dp[node][i]+w:
                        dp[next_node][i] = min(dp[node][i-1],dp[node][i]+w)
                        flag = True
                    
                if flag:
                    heappush(pQueue,(min(dp[next_node]),next_node,node))
        
        
    #print(dp)
    for i in range(1,N+1):
        print(min(dp[i]),end=" ")
        
    print()
	
def main():
    N,M,K = map(int,rl().split())
    graph = [[] for i in range(N+1)]
    
    for _ in range(M):
        u,v,w = map(int,rl().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    findShortestPath(N,M,K,graph)
 
main()
