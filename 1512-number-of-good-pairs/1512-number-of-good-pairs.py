from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        for n in freq.values():
            count += n * (n - 1) // 2
        return count