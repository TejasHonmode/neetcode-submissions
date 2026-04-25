class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        arr = []
        heapq.heapify(arr)
        for num, cnt in freq.items():
            heapq.heappush(arr, (cnt, num))
            if len(arr) > k:
                heapq.heappop(arr)
        
        res = []
        while len(arr):
            res.append(heapq.heappop(arr)[1])
        return res