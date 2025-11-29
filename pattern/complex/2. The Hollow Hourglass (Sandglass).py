# 2. The Hollow Hourglass (Sandglass)

# * * * * * * * * *
#   * *
#     * *
#       * *
#         *
#       * *
#     * *
#   * *
# * * * * * * * * *

def hourglass(n):
    for i in range(n):
        print(" "*i,end=" ")
        if i==0:
            print("* "*(n+1),end="")
        if i==n-1:
            print(" * ")
        else:
            print("* "*2)
    for i in range(n-2,-1,-1):
        print(" "*i,end=" ")
        if i==0:
            print("* "*(n+1),end="")
        if i==n-1:
            print(" * ")
        else:
            print("* "*2)
hourglass(5)