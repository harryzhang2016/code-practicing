/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>outs;
        for(int i = 0; i< nums.size(); i++)
        {
            for(int j = i+1; j < nums.size();j++ )
            {
                if(nums[i]+nums[j]==target)
                {
                    outs.push_back(i);
                    outs.push_back(j);
                }
            }
        }
        return outs;
    }
};
// @lc code=end

