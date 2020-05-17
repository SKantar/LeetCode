# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def kadane(self, A):
        currSum, maxSum = 0, float("-inf")
        for a in A:
            currSum = a if currSum + a < a else (currSum + a)
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubarraySumCircular(self, A):
        nonCirc = self.kadane(A)
        sumA = sum(A)
        maxNon = self.kadane(map(lambda x: -x, A))

        if sumA + maxNon == 0:
            return nonCirc

        return max(nonCirc, sumA + maxNon)

