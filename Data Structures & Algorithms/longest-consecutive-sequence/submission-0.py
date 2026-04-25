class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n in [0,1]:
            return n
        
        res = 0
        mp = defaultdict(int)
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1] + 1 + mp[num+1]
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]

                res = max(mp[num], res)
        return res
        


        