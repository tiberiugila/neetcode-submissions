class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in num_set:
                best = 1
                while (num+best) in num_set:
                    best+=1
                longest = max(longest,best)
        return longest

        