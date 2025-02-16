class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arth(arr):
            arr.sort()
            d = arr[1] - arr[0]
            for i in range(1,len(arr)):
                if arr[i]-arr[i-1]!=d:
                    return False
            return True
        result = []
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            result.append(arth(sub))
        return result  
