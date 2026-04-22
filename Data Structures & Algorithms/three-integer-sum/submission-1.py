class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                addn = nums[l] + nums[r]
                if addn + a < 0:
                    l = l+1
                elif addn + a > 0:
                    r = r - 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

        