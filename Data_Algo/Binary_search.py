# Binary search
# Takes a sequence of numbers and looks through it to find a specific number and returns its position .

def binary_search(sequence, item):
    begin_index = 0  # beginning position of the sequence
    end_index = len(sequence) - 1  # end position of the sequence, have to minus one as python starts at 0 index

    while begin_index <= end_index:  # as long as beginning is lower than end
        midpoint = begin_index + (
                    end_index - begin_index) // 2  # to get the midpoint need to divide it by 2, it needs to be between beginning index and rest of the items in the sequence
        midpoint_value = sequence[midpoint]  # we can get midpoint by just indexing our sequence with the midpoint were getting on line 9
        if midpoint_value == item:  # if we find the item just return back the position
            return midpoint

        elif item < midpoint:  # item value is lower than position we need to change ending index, it is now the
            # element directly to th left of the sequence
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1  # item is greater than the midpoint then we only need to check the items to the right
    return None  # need to return none if the item is not in the sequence


sequence = [2, 3, 4, 6, 7, 8, 9]
item = 7

print(binary_search(sequence, item))
