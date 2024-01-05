def find_triangle_number(n):
    return n * (n + 1) // 2

n = int(input("Enter the value of n: "))
if n < 1:
    raise ValueError("Please enter a positive integer.")

result = find_triangle_number(n)
print(f"The {n}th triangle number is: {result}")
