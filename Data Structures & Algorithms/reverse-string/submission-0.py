class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)
        mid = (l+r) // 2
        for i in range(mid):
            s[i], s[r-1-i] = s[r-1-i], s[i]
        