def first_non_repeating_element(lst):
    # Create a dictionary to store the count of each element in the list.
    element_count = {}

    # Iterate through the list to count the occurrences of each element.
    for num in lst:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Iterate through the list again to find the first non-repeating element.
    for num in lst:
        if element_count[num] == 1:
            return num

    # If no non-repeating element is found, return None.
    return None

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 5, 4]
result = first_non_repeating_element(my_list)

if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found in the list.")