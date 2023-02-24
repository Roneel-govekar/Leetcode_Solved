class Solution():
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten=[]
        #print("col",len(mat[0]))
        #print("row",len(mat))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                flatten.append(mat[i][j])
        #print(flatten)
        
        k=0
        #print(Matrix)
        if r*c != len(mat[0])*len(mat):
            return mat
        
        Matrix = [[0 for x in range(c)] for y in range(r)] 
        for i in range(r):
            for j in range((len(mat[0])*len(mat))//r):
                Matrix[i][j]=flatten[k]    
                k+=1 
            
        return Matrix