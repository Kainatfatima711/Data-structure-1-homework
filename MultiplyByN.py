def multiply_one_iteration(n, m):
    return n * m

def multiply_n_iteration(n, m):
    result = 0
    for _ in range(m):
        result += n
    return result

n = int(input("Enter first number (n): "))
m = int(input("Enter second number (m): "))

print("Multiplication using 1 iteration:", multiply_one_iteration(n, m))
print("Multiplication using N iteration:", multiply_n_iteration(n, m))

