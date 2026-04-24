"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        end_times = []
        for interval in intervals:
            if len(end_times) and end_times[0] <= interval.start:
                heapq.heappop(end_times)
            heapq.heappush(end_times, interval.end)
        
        return len(end_times)

        