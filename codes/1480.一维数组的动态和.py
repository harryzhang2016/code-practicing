#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list_sum = []
        cur_sum_res = 0
        for num in nums:
            cur_sum_res += num
            list_sum.append(cur_sum_res)
        return list_sum
# @lc code=end

