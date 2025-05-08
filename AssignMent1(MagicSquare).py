import numpy as np

def generate_magic_square(n):
    if n % 2 == 0:
        print("Only odd order magic squares are supported")
        return
    
    magic_square = np.zeros((n, n), dtype=int)
    
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i, new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    
    print_magic_square(magic_square)

def print_magic_square(square):
    for row in square:
        print(" ".join(str(num).rjust(2) for num in row))
    print()

# Example usage
generate_magic_square(3)  # Generate a 5x5 magic square