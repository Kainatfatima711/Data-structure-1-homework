def rightmost_set_bit(n):
   
    if n == 0:
        return 0  

    position = 1
    while (n & 1) == 0:
        n = n >> 1  
        position += 1
    return position

print("=== FirstSetBit Project ===")
num = int(input("Enter a number: "))

pos = rightmost_set_bit(num)
if pos == 0:
    print("No set bits found in", num)
else:
    print("Rightmost set bit is at position:", pos)













