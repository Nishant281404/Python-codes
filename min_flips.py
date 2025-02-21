class Solution:
    def minFlips(self, S):
        f1 = 0
        f2 = 0
        for i in range(0,len(S)):
            if i%2 == 0 and S[i] != '0'  :
                f1 += 1
            if i%2 == 1 and S[i] != '1':
                f1 += 1
        for i in range(0,len(S)):
            if i%2 == 0 and S[i] != '1':
                f2 += 1
            if i%2 == 1 and S[i] != '0':
                f2 += 1
        return min(f1,f2)  
