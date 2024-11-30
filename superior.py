def sum_of_divisors(n):
    """Function to calculate the sum of divisors of a number"""
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def is_superior_number(n):
    """Check if a number is a superior number"""
    visited = []
    current = n
    while current != 1 and current not in visited:
        visited.append(current)
        current = sum_of_divisors(current)
        if current == n:
            return True 
    return False

n = 12
if is_superior_number(n):
    print(f"{n} is a superior number.")
else:
    print(f"{n} is not a superior number.")
