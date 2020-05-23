# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

import collections
class Solution:
    def _equal(self, curr: dict, ref: dict) -> bool:
        for key in curr:
            if key not in ref and curr[key]:
                return False
            if curr[key] != ref[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        ref = collections.Counter(s1)
        curr = collections.defaultdict(lambda: 0)
        for i in range(len(s1)):
            curr[s2[i]] += 1

        for i in range(len(s2) - len(s1)):
            if self._equal(curr, ref):
                return True
            curr[s2[i]] -= 1
            curr[s2[i + len(s1)]] += 1
        else:
            if self._equal(curr, ref):
                return True

        return False