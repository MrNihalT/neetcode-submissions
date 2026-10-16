class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ind = {}
        ind2 = {}
        for i in s:
            if i in ind:
                ind[i] +=1
            else:
                ind[i] = 1

        for i in t:
            if i in ind2:
                ind2[i] +=1
            else:
                ind2[i] = 1
        

        if ind == ind2:
            return True

        
        return False
        