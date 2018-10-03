class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_num = set(nums)
        
        for i in range(0, len(nums)+1):
            if i not in all_num:
                return i
            
        return None
