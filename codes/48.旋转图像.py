from typing import List
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        new = [[matrix[i][j] for j in range(n)] for i in range(n)]
        #(j, n-1-i)
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = new[i][j]
# @lc code=end

