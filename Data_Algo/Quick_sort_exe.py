# takes an unsorted sequence and sorts it either in ascending or descending order
# start by taking unsorted sequence and choosing a pivot(number to base comparison of all numbers on)
# iterate through the rest of numbers in the list, comparing if its less or greater than the pivot
# less numbers go into one list and greater into one list, when its sorted lock it in
# do the whole process again, choosing an optimal pivot


# WRITE A PYTHON PROGRAM TO QUICK SORT A SEQUENCE

def quick_sort(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop()

    item_greater = []
    item_lesser = []

    for item in sequence:
        if item > pivot:
            item_greater.append(item)

        else:
            item_lesser.append(item)
    return quick_sort(item_lesser) + [pivot] + quick_sort(item_greater)


print(quick_sort([2,3,5,7,1,92,3,3]))
print(quick_sort([5, 2, 5]))
