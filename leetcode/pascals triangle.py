class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle=[[1],[1,1],[1,2,1]]
        if rowIndex<=2:
            return triangle[rowIndex]
        
        for i in range(3,rowIndex+1):
            new=[1]
            for j in range(1,len(triangle[i-1])):
                new.append(triangle[i-1][j-1]+triangle[i-1][j])
            new.append(1)
            triangle.append(new)
        return triangle[rowIndex]
                