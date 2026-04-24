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
        heapq.heapify(end_times)
        for interval in intervals:
            heapq.heappush(end_times, interval.end)
            if end_times[0] <= interval.start:
                heapq.heappop(end_times)
        
        return len(end_times)

        