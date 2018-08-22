class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        matrix=[]
        one_row=[]
        for i in nums:
            for j in i:
                one_row.append(j)
        if r*c == len(one_row):
            for i in range(0,len(one_row),c):
                matrix.append(one_row[i:i+c])
            return matrix
        else:
            return nums
