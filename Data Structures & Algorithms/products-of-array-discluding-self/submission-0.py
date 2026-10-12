class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res=[1] * n

        preffix = 1
        for i in range(n):
            res[i] *= preffix
            preffix *= nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


        