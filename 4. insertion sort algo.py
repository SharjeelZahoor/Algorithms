def insertion_sort(lst, n):
    # Iterate over the list starting from the second element
    for i in range(1, n):
        # Store the current element in a temporary variable
        temp = lst[i]
        # Set j to the index of the element just before the current element
        j = i - 1

        # Move elements of lst[0..i-1], that are greater than temp, to one position ahead of their current position
        while j >= 0:
            if temp < lst[j]:
                # Shift the element one position to the right
                lst[j + 1] = lst[j]
                # Move to the previous element
                j -= 1
            else:
                break

        # Place temp in its correct position
        lst[j + 1] = temp

    # Return the sorted list
    return lst


# Example usage
lst = [2, 4, 1, 5, 3]
n = len(lst)
print(insertion_sort(lst, n))
