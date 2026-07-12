class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp bottom up + greedy hybrid
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        goal = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                dp[i] = True
                goal = i
            else:
                continue
        
        return dp[0]
        