def myfunction1(n):
    if n <= 0:
        return
    for _ in range(int(n)+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

def myfunction2(n):
    if n <= 1:
        return
    print("Codingal")
    myfunction2(n-1)

def print_complexity():
    print("\n--- Recurrence Relations and Complexity ---\n")
    print("1. myfunction1(n):")
    print("   Recurrence: T(n) = T(n/2) + T(n/3) + O(n)")
    print("   Time Complexity: O(n)")
    print("   Space Complexity: O(log n)\n")
    
    print("2. myfunction2(n):")
    print("   Recurrence: T(n) = T(n-1) + O(1)")
    print("   Time Complexity: O(n)")
    print("   Space Complexity: O(n)\n")

def print_recursion_tree(n, prefix="", depth=0, max_depth=5):
    if n <= 0 or depth > max_depth:
        return
    print(f"{prefix}{n:.2f}")
    print_recursion_tree(n/2, prefix+"  ", depth+1, max_depth)
    print_recursion_tree(n/3, prefix+"  ", depth+1, max_depth)

def main():
    n1 = float(input("Enter n (float) for myfunction1: "))
    n2 = int(input("Enter n (integer) for myfunction2: "))

    print("\n--- Running myfunction1 ---")
    myfunction1(n1)

    print("\n--- Running myfunction2 ---")
    myfunction2(n2)

    print_complexity()

    print("--- Recursion Tree of myfunction1 (text) ---")
    print_recursion_tree(n1)

if __name__ == "__main__":
    main()
