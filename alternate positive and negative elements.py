class Solution:
    def rearrange(self,arr):
        p = [num for num in arr if num >= 0]
        n = [num for num in arr if num < 0]
        k=0
        i,j = 0,0
        while i<len(p) and j<len(n):
            arr[k] = p[i]
            i+=1 
            k+=1
            arr[k] = n[j]
            j+=1 
            k+=1
        while i < len(p):
            arr[k] = p[i]
            k += 1
            i += 1
        while j<len(n):
            arr[k] = n[j]
            k+=1
            j+=1
