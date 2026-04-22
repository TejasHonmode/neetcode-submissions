class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;

        arr = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax < rmax:
                arr += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                arr += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
            
        return arr
        

        