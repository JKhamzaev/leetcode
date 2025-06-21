class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sol =[]
        for i in range(len(nums)):
            if nums[i] != val:
                sol.append(nums[i])
            
        for i in range(len(sol)):
            nums[i] = sol[i]

        return len(sol)