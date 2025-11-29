# 3. The Sequential Spiral Matrix (1 to $N^2$)

# 1  2  3  4
# 12 13 14  5
# 11 16 15  6
# 10  9  8  7
n=4

def matrix(n):
    top,bottom,left,right=0,3,0,3
    val=1
    mat = [[0] * n for _ in range(n)]
    
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            mat[top][i]=val
            val+=1
        top+=1
        for i in range(top,bottom+1):
            mat[i][right]=val
            val+=1
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                mat[bottom][i]=val
                val+=1
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                mat[i][left]=val
                val+=1
            left+=1
    return mat



matrixs=matrix(4)

for i in matrixs:
    print(i)
