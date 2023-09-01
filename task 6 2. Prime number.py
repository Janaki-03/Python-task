def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_list(input_list):
    prime_numbers = []
    for num in input_list:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
my_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = find_primes_in_list(my_list)

print("Prime numbers in the list:", prime_numbers)