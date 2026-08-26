class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre in prerequisites:
            adjlist[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)

            for nei in adjlist[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ans if len(ans) == numCourses else []
        