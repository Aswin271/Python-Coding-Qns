def is_happy_number(n):
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))
    
    seen_numbers = set()  # To track numbers we've already seen
    
    while n != 1:
        n = sum_of_squares(n)
        
        if n in seen_numbers:
            return False  # Cycle detected, hence not a happy number
        
        seen_numbers.add(n)  # Add the current number to the set of seen numbers
    
    return True

num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is a happy number!")
else:
    print(f"{num} is not a happy number.")
