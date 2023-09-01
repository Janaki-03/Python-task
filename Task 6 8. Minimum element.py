def find_minimum_in_sorted_list(sorted_list):
    if not sorted_list:
        return None  # Return None for an empty list
    return sorted_list[0]

# Example usage:
sorted_list = [1, 2, 3, 4, 5]

minimum = find_minimum_in_sorted_list(sorted_list)

if minimum is not None:
    print("The minimum element in the sorted list is:", minimum)
else:
    print("The list is empty.")