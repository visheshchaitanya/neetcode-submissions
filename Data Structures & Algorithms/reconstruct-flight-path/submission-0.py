from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)

        ans = []

        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)

            ans.append(src)

        dfs("JFK")

        return ans[::-1]