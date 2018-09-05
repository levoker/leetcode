class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_len = 1
        prev = nums[0]
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > prev:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
            prev = nums[i]
        return max(curr_len, max_len)
