# 421. Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, n):
        curr = self.root
        for i in range(31, -1, -1):
            currBit = (n >> i) & 1
            if currBit not in curr.children:
                curr.children[currBit] = TrieNode()
            curr = curr.children[currBit]

    def getMaxDiff(self, n):
        curr, currSum = self.root, 0
        for i in range(31, -1, -1):
            currBit = (n >> i) & 1
            if currBit ^ 1 in curr.children:
                currBit ^= 1
                currSum += 1 << i
            curr = curr.children[currBit]
        return currSum

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        for n in nums:
            trie.insert(n)

        maxXOR = 0
        for n in nums:
            maxXOR = max(maxXOR, trie.getMaxDiff(n))
        return maxXOR

s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
