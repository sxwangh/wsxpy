# 度：一个顶点连接了几条边  （若共有n个节点 ：则中心节点的度 = n -1 ; 其他节点的度 = 1）
import collections
from typing import List


class Solution:
    @staticmethod
    def findCenter(edges: List[List[int]]) -> int:
        n = len(edges) + 1
        degrees = [0] * (n + 1)
        for x, y in edges:
            degrees[x] += 1
            degrees[y] += 1
        for i, d in enumerate(degrees):
            if d == n - 1:
                return i


point = Solution.findCenter([[1, 2], [2, 3], [4, 2]])
point2 = Solution.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]])
print(point)
print(point2)
