# twosum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    # O(n^2)
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numMap = {}

        for index, value in enumerate(nums): 
            diff = target - value # 7 = 9-2
            if diff in nums:
                diff_i = nums.index(diff)
                if index != diff_i:
                    return [index, diff_i]

    # O(n)
    def twoSum(self, nums, target):
        # to save indices of values 
        numMap = {} 
            
        for index, value in enumerate(nums):
            diff = target - value # 7 = 9-2

            if diff not in numMap:
                numMap[value] = index
            else: return [index, numMap[diff]]
   
            
