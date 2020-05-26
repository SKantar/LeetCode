# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

class Solution:
    def findMaxLength(self, nums):
        _store = {0: Interval(-1, -1)}
        _max = _curr = 0

        for i in range(len(nums)):
            _curr = _curr + (1 if nums[i] == 1 else -1)
            if _curr in _store:
                _store[_curr].end = i
            else:
                _store[_curr] = Interval(i, i)

            _max = max(_max, _store[_curr].end - _store[_curr].start)
        return _max