class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n in [0,1]:
            return n
        
        res = 0
        mp = defaultdict(int)
        for num in nums:
            if not mp[num]:
                left = mp[num-1]
                right = mp[num+1]
                mp[num] = left + 1 + right
                mp[num - left] = mp[num]
                mp[num + right] = mp[num]

                res = max(mp[num], res)
        return res

        