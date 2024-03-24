#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = int(''.join(str(d) for d in digits))+1
        n = len(digits)
        num = sum(d*10**(n-i-1) for i, d in enumerate(digits))+1
        return [int(n) for n in str(num)]
# @lc code=end

