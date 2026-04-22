class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heapq.heapify_max(stones)

        while len(stones) > 1:
            l1 = heapq.heappop_max(stones)
            l2 = heapq.heappop_max(stones)

            if l1 != l2:
                new_stone = abs(l1-l2)
                heapq.heappush_max(stones, new_stone)
            else:
                continue

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

