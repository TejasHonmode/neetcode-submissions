class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = {}
        for num in nums:
            if maps.get(num):
                return True
            else:
                maps[num] = 1
        return False
        