class Solution:

    def b_search(self, l, r, nums, target):
        if l > r:
            return -1

        mid = (r + l) // 2
       
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.b_search(mid+1, r, nums, target)

        return self.b_search(l, mid-1, nums, target)  

    def search(self, nums: List[int], target: int) -> int:
        return self.b_search(0, len(nums) - 1, nums, target)
            