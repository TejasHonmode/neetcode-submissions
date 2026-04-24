class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if len(intervals) == 1:
            return res
        intervals.sort()
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < last_end:
                res += 1
                last_end = min(end, last_end)
            else:
                last_end = end
        return res