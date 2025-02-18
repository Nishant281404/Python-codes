class Solution:
    def merge(self, S1, S2):
        s = ""
        i,j=0,0
        while i<len(S1) and j<len(S2):
            s += S1[i]
            s += S2[j]
            i += 1
            j += 1
        while i != len(S1):
            s += S1[i]
        while j != len(S2):
            s += S2[j]
        return s    # can generate TLE
################################### APPROACH 2###########################       
        
class Solution:
    def merge(self, S1, S2):
        res = []
        i,j = 0,0
        while i<len(S1) and j<len(S2):
            res.append(S1[i])
            res.append(S2[j])
            i+=1
            j+=1
        res.append(S1[i])    
        res.append(S2[j])
        return "".join(res)
        # code here
