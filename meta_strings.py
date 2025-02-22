####### Approach using a extra space and numerical representation ##################

class Solution:
    def metaStrings(self, S1, S2):
        f = [0] * 26
        if len(S1) != len(S2):
            return 0
        for i in range(0,len(S1)):
            f[ord(S1[i]) - ord('a')] += 1
            f[ord(S2[i]) - ord('a')] -= 1
        for j in range(0,26):
            if f[j] != 0:
                return 0
        c = []        
        for k in range(0,len(S1)):
            if S1[k] != S2[k]:
                c.append(k)
        if len(c) != 2:
            return 0
        i,j = c
        if S1[i] == S2[j] and S1[j] == S2[i]:
            return 1
        else: 
            return 0
