print("Enter values for A, B, C (0 or 1 only)")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

gate1 = A & B          
gate2 = B | C       
gate3 = B & C          

gate4 = gate2 & gate3 
Q = gate1 | gate4     

print("\nCircuit Output:")
print("Q =", Q)