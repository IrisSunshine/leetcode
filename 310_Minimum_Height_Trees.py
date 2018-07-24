
# coding: utf-8

# In[ ]:

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1: return [0]
        
        adj=[set() for _ in range(n)]

        for i,j in edges: 
            adj[i].add(j)
            adj[j].add(i)
            
        leaves=[]
        for i in range(n):
            if len(adj[i])==1: 
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: 
                    newLeaves.append(j)
            leaves = newLeaves
            
        return leaves
