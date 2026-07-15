class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #own
        prod, zeros = 1, 0
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros >= 2:
                    return [0]*len(nums)
            else:
                prod *= num
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zeros == 1:
                if num == 0:
                    res[i] = prod
                    return res
            else:
                res[i] = prod // num
        return res
            