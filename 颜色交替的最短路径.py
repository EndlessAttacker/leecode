from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        try:
            for x, y in blueEdges:
                g[x].append((y, 1))
        except:
            pass
        # print(g)
        dis = [-1] * n #距离#
        vis = {(0, 0), (0, 1)} #去重#
        q = deque([(0, 0), (0, 1)])#初始队列红蓝#
        level = 0 
        while q:
            for _ in range(len(q)):
                i,color = q.popleft()

                if dis[i] == -1:
                    dis[i] = level
                color = 1 - color
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
                        
            level += 1
        return dis        
        # g = [defaultdict(list), defaultdict(list)]
        # for i, j in redEdges:
        #     g[0][i].append(j)
        # for i, j in blueEdges:
        #     g[1][i].append(j)
        # ans = [-1] * n
        # vis = set()
        # q = deque([(0, 0), (0, 1)])
        # d = 0
        # while q:
        #     for _ in range(len(q)):
        #         i, c = q.popleft()
        #         if ans[i] == -1:
        #             ans[i] = d
        #         vis.add((i, c))
        #         c ^= 1
        #         for j in g[c][i]:
        #             if (j, c) not in vis:
        #                 q.append((j, c))
        #     d += 1
        # return ans

        
        # g = [defaultdict(list), defaultdict(list)]
        # for i, j in redEdges:
        #     g[0][i].append(j)
        # for i, j in blueEdges:
        #     g[1][i].append(j)
        #     dis = [-1] * n
        #     vis = set()
        #     q = deque([(0,0),(0,1)])
        #     d = 0
        #     while q:
        #         for _ in range(len(q)):
        #             i,c = q.popleft()
        #             print(i)
        #             if dis[i] == -1:
        #                 dis[i] = d
        #             vis.add((i,c))
        #             c = 1 - c
        #             for j in g[c][i]:
        #                 if (j,c) not in vis:
        #                     q.append((j,c))
        #         d = d + 1
        #     return dis
s = Solution()
result = s.shortestAlternatingPaths(6,[[0,2],[0,5],[2,6]],[[]])
print(result)

