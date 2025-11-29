# Number Bridge

# 1 2 3 4 5 4 3 2 1 
# 1 2 3 4   4 3 2 1 
# 1 2 3       3 2 1 
# 1 2           2 1 
# 1               1

def print_number_bridge(n):
    for i in range(n):
        for j in range(1,n+1-i):
            print(j,end=" ")
        print("  "*((i*2)-1),end="")
        
        for j in range(n-i,0,-1):
            if j==n:
                continue
            print(j,end=" ")

        print()

print_number_bridge(5)
