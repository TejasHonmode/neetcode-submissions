class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash table
        if len(s) != len(t):
            return False
        
        ht = [0] * 26
        for i in range(len(s)):
            ht[ord(s[i]) - ord('a')] += 1 
            ht[ord(t[i]) - ord('a')] -= 1 
        
        for val in ht:
            if val != 0:
                return False
        return True
        