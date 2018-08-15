class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            if nums[begin] == val:
                nums[begin] = nums[end]
                end -= 1
            else:
                begin += 1
        return end+1
        
        # val = 2
        # list = [2,3,4,5,2]
