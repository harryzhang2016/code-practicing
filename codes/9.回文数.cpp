/*
 * @lc app=leetcode.cn id=9 lang=cpp
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        
        int i = 0;
        if (x < 0 || (x % 10 == 0)&&(x!=0)) {
            return false;
        }
        if(x<10)
        {
            return true;
        }
        
        while(x>i)
        {
            i = i*10 + x%10;
            x/=10;
        }
        bool a = (x == i) ||(x==i/10);

        return a;
        
    }
};
// @lc code=end

