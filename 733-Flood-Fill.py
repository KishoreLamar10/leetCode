class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        old = image[sr][sc]
        if old == color:
            return image
        def dfs(sr,sc):
            if sr < 0 or sr >= ROWS or sc < 0 or sc >= COLS or image[sr][sc] != old:
                return
            image[sr][sc] = color
            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
        dfs(sr,sc)
        return image
        




        