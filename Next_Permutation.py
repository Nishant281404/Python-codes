class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # fuction to reverse nums
        def reverse(nums):
            for i in range(0,len(nums)):
                nums[i],nums[len(nums)-1] = nums[len(nums)-1] , nums[i]

        # find location of pivot element        
        p = -1
        for j in range(len(nums)-2,-1,-1):
            if nums[j]<nums[j+1]:
                p = j
                break
       # if permutation is last 
        if p == -1:
            nums.reverse()
            return 
       # swapping last element
        for  k in range(len(nums)-1, p,-1):
            if nums[k]>nums[p]:
                nums[k],nums[p] = nums[p],nums[k]
                break
        q = p+1
        w = len(nums)-1
        while q<=w:
            nums[q],nums[w] = nums[w] , nums[q]
            q+=1
            w-=1
