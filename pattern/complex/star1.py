
# **********
# **** ****
# *** ***
# ** **
# * *
# * *
# ** **
# *** ***
# **** ****
# **********

def star(n):
    for i in range(n,0,-1):
        print("*"*i,end="")
        if i!=n:
            print(" ",end="")
        print("*"*i)

    for i in range(1,n+1):
        print("*"*i,end="")
        if i!=n:
            print(" ",end="")
        print("*"*i)

star(5)