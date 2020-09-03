学习笔记



[最长有效括号](https://github.com/luobangkui/algorithm012/blob/master/Week_09/32_longestValidParentheses.py)

[解码方法](https://github.com/luobangkui/algorithm012/blob/master/Week_09/91_numDecodings.py)

[不同的子序列](https://github.com/luobangkui/algorithm012/blob/master/Week_09/115_numDistinct.py)

[最长上升子序列](https://github.com/luobangkui/algorithm012/blob/master/Week_09/300_lengthOfLIS.py)


#### 高级动态规划

* 一般比较复杂，需要更多维度的dp数组来进行处理
* 一般的dp数组，看是否可以进行空间优化，比如二维数组，dp[i][j]只和它的左边和上边有关联，则可以优化为一维dp
* 最长有效括号，注意'))'和'()'的判断，同时注意它的状态转移方程;解码方法，考虑到所有可能的情况，特殊要考虑到```s[i]=='0'```
以及```s[i-1] == '0'```的情况


#### 字符串相关

* 字符串基础问题，代码要写清晰漂亮
* 字符串操作问题
* 异位词问题（一般是通过计数方式去做）
* 回文串验证
* 字符串和动态规划结合
* 最长子串、子序列问题
* 字符串匹配算法
