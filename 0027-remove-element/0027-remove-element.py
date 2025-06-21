class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums) - 1
        while j > -1 and nums[j]==val:
                j -= 1
        for i in range(j):
            while j > -1 and nums[j]==val:
                j -= 1
            if nums[i] == val:
                if j <= i:
                    break
                s = nums[i]
                nums[i] = nums[j]
                nums[j] = s
                j-=1
        print(j+1)
        return j+1