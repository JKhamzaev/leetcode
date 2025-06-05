class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        s=0
        for i in d.values():
            if i > 1:
                n = i
                s += n*(n-1)/2
        return s

            