class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        m , n = len(mat), len(mat[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        while q:
            r,c = q.popleft()
            directions = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]

            for nr,nc in directions:
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr,nc))
        return mat

        