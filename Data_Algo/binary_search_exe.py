# binary search involves looking through an already sorted list and checking if a number is there, then returning the position
# we get the middle point of the sequence
# if item is greater than the midpoint, we search to the right of the sequence
# if item is less than the midpoint we search to the left of the sequence

# WRITE A PYTHON PROGRAM FOR A BINARY SEARCH

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None


sequence_a = [2, 3, 4, 5, 6, 7, 8, 9]
item_a = 8
print(binary_search(sequence_a, item_a))
