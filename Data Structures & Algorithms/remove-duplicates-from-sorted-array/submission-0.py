class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        l = r = 0
        n = len(nums)
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1
        return l

        