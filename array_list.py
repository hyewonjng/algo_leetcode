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
   
            

# threeSum
# nums = [-1,0,1,2,-1,-4]
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        s = set()
        output = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    # res_set.add(tuple([nums[i], nums[j], nums[k]]))
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output
    