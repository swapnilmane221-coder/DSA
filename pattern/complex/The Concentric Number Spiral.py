# The Concentric Number Spiral
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

def print_concentric_pattern(n):
    size = 2 * n - 1
    
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            min_dist = min(top, left, bottom, right)
            value = n - min_dist
            print(value, end=" ")
        print()


print_concentric_pattern(4)