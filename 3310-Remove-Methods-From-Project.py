class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = [0] * n
        visited = [False] * n

        for u,v in invocations:
            graph[u].append(v)
            indegree[v] += 1
        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                indegree[nei] -= 1
                if not visited[nei]:
                    dfs(nei)
        
        dfs(k)
        for i in range(n):
            if visited[i] and indegree[i] > 0:
                return list(range(n))

        ans = []

        for i in range(n):
            if not visited[i]:
                ans.append(i)
        return ans