# The Concentric Number Spiral
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

def print_concentric_pattern(n):
    # The size of the grid is always 2*n - 1
    # Example: if n=4, size is 7x7
    size = 2 * n - 1
    
    # Iterate through every row (i) and column (j)
    for i in range(size):
        for j in range(size):
            
            # Calculate distances to all four sides
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            
            # Find the minimum distance to an edge
            min_dist = min(top, left, bottom, right)
            
            # The value is N minus that minimum distance
            value = n - min_dist
            
            # Print the value with a space, stay on same line
            print(value, end=" ")
        
        # Move to the next line after finishing a row
        print()

# Driver Code
n = 4
print_concentric_pattern(n)