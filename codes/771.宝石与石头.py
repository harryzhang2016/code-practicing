#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        nums = 0
        for stone in stones:
            if jewels.find(stone) != -1:
                nums += 1
        return nums
# @lc code=end

