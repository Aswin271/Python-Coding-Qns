
num = int(input("Enter an integer: "))
binary = ""

# Handle the case for zero
if num == 0:
    binary = "0"
    
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary 
    num = num // 2 
    
print("Binary representation:", binary)
