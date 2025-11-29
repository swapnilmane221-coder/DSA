def pascal_triangle(n):
    
    for i in range(n):
        val=1
        print(" "*(n-i-1),end=" ")
        for j in range(i+1):
            print(val,end=" ")
            val=val*(i-j)//(j+1)   
        print()



pascal_triangle(5)