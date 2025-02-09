def mirrored_triangle(n):
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # Move to the next line

# Example usage
n = 5  # Height of the triangle
mirrored_triangle(n)
