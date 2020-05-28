# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num):
        ans = [0]
        if num > 0:
            ans.append(1)
        curr = end = 0
        for i in range(2, num + 1):
            if curr == end:
                end = i
                curr = 0

            ans.append(1 + ans[curr])
            curr += 1

        return ans