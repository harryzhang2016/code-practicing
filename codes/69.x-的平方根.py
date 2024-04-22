#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            if i*i <= x and (i+1)*(i+1)>x:
                return i
# @lc code=end

