from typing import List
#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums)
        for i, num in enumerate(nums):
            sum_right-=num
            if sum_left == sum_right:
                return i
            else:
                sum_left += num
        return -1
# @lc code=end
                
if __name__ == "__main__":
    s = Solution()
    res = s.pivotIndex([1,7,3,6,5,6])
    print(res)
