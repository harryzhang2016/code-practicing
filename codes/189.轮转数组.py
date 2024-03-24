from typing import List
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def plusk(pk,val,lists):
            if int(pk/self.k)==self.end:
                return
            index=pk%self.n
            temp=lists[index]
            lists[index] = val
            val=temp
            plusk(self.k+pk, val, lists)

        self.n=len(nums)
        self.k = k%self.n
        if self.k==0:
            return
        iter = 1
        self.end=self.n+1
        for i in range(1,self.k):
            if i*self.n%self.k==0:
                iter=int(self.k/i)
                self.end=int(i*self.n/self.k)+1
                break
        for i in range(iter):
            plusk(self.k+i,nums[i],nums)
        print(nums)
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4,5,6],3)