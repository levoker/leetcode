class Solution:
    def isMonotonic(self, A):
        return len(A) == 1 or self.checkDecreasing(A) or self.checkIncreasing(A)
        """
        :type A: List[int]
        :rtype: bool
        """

    def checkDecreasing(self, A):
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                return False
        return True

    def checkIncreasing(self, A):
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                return False
        return True
