# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        iA = iB = 0
        ans = list()
        while iA < len(A) and iB < len(B):
            start = max(A[iA][0], B[iB][0])
            end = min(A[iA][1], B[iB][1])
            if start <= end:
                ans.append([start, end])

            if A[iA][1] > B[iB][1]:
                iB += 1
            else:
                iA += 1
        return ans
