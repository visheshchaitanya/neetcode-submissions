class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        