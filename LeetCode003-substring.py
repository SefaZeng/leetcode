class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s为空的情况
        if not s:
            return 0
        ans = 1 # 非空子字符串的长度最小为1
        substr = "" # 子字符串
        for item in s:
            if item not in substr:
                substr += item
                ans = max(ans,len(substr))
            else:
                substr += item
                substr = substr[substr.index(item)+1:]
        return ans
