class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        k = sum(nums)
        sum_two = 0
        for i in nums:
            while  i > 9 :
                dig = i % 10
                sum_two += dig
                i //= 10
            sum_two += i
        return abs(k - sum_two)            

        