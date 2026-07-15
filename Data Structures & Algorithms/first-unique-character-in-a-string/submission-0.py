class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        for i, num in enumerate(s):
            if num not in count:
                count[num] = i
            else:
                count[num] = n
            
        min_idx = n
        for num in count:
            if count[num] == n:
                continue
            else:
                min_idx = min(min_idx, count[num])
        
        if min_idx == n:
            return -1
        else:
            return min_idx
