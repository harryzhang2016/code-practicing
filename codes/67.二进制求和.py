#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        sum = 0
        res = ''
        for i, num in enumerate(a):
            sum += int(num)*(2**(len_a-i-1))
        for j, n in enumerate(b):
            sum += int(n)*(2**(len_b-j-1))
        while sum>0:
            r = sum%2
            sum = sum//2
            res = str(r)+res

        return res if res != '' else '0'
# @lc code=end

if __name__ == "__main__":
    Solution().addBinary("11","1")