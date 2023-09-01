def sum_of_first_and_last_digit(number):
    # Convert the number to a string to easily access its digits.
    number_str = str(number)

    # Extract the first and last characters and convert them to integers.
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])

    # Calculate the sum of the first and last digits.
    result = first_digit + last_digit

    return result

# Example usage:
input_number = 12345
result = sum_of_first_and_last_digit(input_number)

print("Sum of the first and last digits:", result)