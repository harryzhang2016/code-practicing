#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_assets = 0
        for list_m in accounts:
            assets = sum(list_m)
            if assets > max_assets:
                max_assets =assets
        return max_assets
# @lc code=end

