class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for k in range(0,len(matrix)):
            l = 0 
            r = len(matrix)-1 
            while l<=r:
                temp = matrix[k][l]
                matrix[k][l] = matrix[k][r]
                matrix[k][r] = temp
                l+=1
                r-=1
        

        
        
