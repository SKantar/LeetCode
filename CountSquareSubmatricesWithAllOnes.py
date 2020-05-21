# 1277. Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        N, M = len(matrix), len(matrix[0])
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        total = 0

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if matrix[i - 1][j - 1] == 0:
                    continue

                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                total += dp[i][j]
        return total


