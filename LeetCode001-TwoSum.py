class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_num = sorted(nums)

        left = 0
        right = len(nums)-1
        res = []
        while(left<right):
            sum = sorted_num[left] + sorted_num[right]
            if sum == target:
                break;
            elif sum>target:
                right-=1
            else:
                left+=1

        if left == right:
            return -1,-1
        else:
            pos1 = nums.index(sorted_num[left])
            pos2 = nums.index(sorted_num[right]) #题目要求返回的是以0为起始
            if pos1==pos2:
                pos2 = nums[pos1+1:].index(sorted_num[right])+pos1+1 #如果两者相同，说明数值一样，查到的index一样，以pos1的后一位为起始搜索

            return min(pos1,pos2),max(pos1,pos2)
        
