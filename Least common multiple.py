#Input two numbers
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

#Find the larger number
if num1 > num2:
    greater = num1
else: 
    greater = num2
#Loop until LCM found
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater = greater

print("LCM is" , lcm)