# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/

class Solution:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def findRedundantConnection(self, edges):
        N = len(edges)
        parent, rank = list(range(N)), [0] * N

        for u, v in edges:
            x = self.find(parent, u - 1)
            y = self.find(parent, v - 1)

            if x == y:
                return [u, v]

            self.union(parent, rank, x, y)