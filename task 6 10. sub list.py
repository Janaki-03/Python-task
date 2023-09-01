def has_sublist_with_sum_zero(lst):
    cumulative_sum = 0
    seen_sums = set()

    for num in lst:
        cumulative_sum += num

        # If the cumulative sum repeats or if the current number is 0, there's a sub-list with sum 0.
        if cumulative_sum == 0 or cumulative_sum in seen_sums or num == 0:
            return True

        seen_sums.add(cumulative_sum)

    return False

# Example usage:
my_list = [4,2,-3,1,6]
result = has_sublist_with_sum_zero(my_list)
if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("No sub-list with a sum equal to zero found.")