def find_duplicates_in_three_lists(list1, list2, list3):
    # Convert the lists to sets for faster duplicate detection.
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find the intersection of the three sets to get the common elements.
    common_elements = set1.intersection(set2, set3)

    return list(common_elements)

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

duplicates = find_duplicates_in_three_lists(list1, list2, list3)

if duplicates:
    print("Duplicates in the three lists:", duplicates)
else:
    print("No duplicates found in the three lists.")
    