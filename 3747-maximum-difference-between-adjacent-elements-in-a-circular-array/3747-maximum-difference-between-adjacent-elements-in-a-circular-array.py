class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = 0
        for i in range(0, len(nums)):
            if abs(nums[i]-(nums[i-1])) > maxSum:
                maxSum = abs(nums[i]-(nums[i-1]))

        return maxSum