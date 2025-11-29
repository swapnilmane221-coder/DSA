# 2. The Hollow Diamond Inscribed in a Rectangle

# * * * * * * * * *
# * * * * * * * *
# * * * * * *
# * * * *
# * *
# * * * *
# * * * * * *
# * * * * * * * *
# * * * * * * * * *


def print_hollow_diamond_pattern(n):
    i=0
    while i<n:
        for j in range(n-i):
            print("*",end=" ") 
        print()
        if i!=0:
            i+=2
        else:
            i+=1
    i-=4
    while i>=0:
        for j in range(n-i):
            print("*",end=" ") 
        print()
        if i!=1:
            i-=2
        else:
            i-=1





print_hollow_diamond_pattern(9)