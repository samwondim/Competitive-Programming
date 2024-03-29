class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])

        transpose = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                transpose[j][i] = matrix[i][j]
        
        return transpose
