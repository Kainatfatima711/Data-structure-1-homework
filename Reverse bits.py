num = int(input("Enter your original number: "))

binary = bin(num)[2:]

reversed_binary = binary[::-1]

reversed_number = int(reversed_binary, 2)

print("Binary:", binary)
print("Reversed Binary:", reversed_binary)
print("Reversed Number:", reversed_number)
