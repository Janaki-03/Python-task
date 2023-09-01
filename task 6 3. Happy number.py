def is_happy_number(n):
    seen = set()
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True

def count_happy_numbers_in_list(input_list):
    count = 0
    for num in input_list:
        if is_happy_number(num):
            count += 1
    return count

# Example usage:
my_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = count_happy_numbers_in_list(my_list)

print("Number of happy numbers in the list:", happy_count)