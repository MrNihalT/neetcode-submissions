class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ind = {}
        ind2 = {}

        for i in range(len(s)):
            ind[s[i]] = 1 + ind.get(s[i],0)
            ind2[t[i]] = 1 + ind2.get(t[i],0)

        
        return ind == ind2
        
        