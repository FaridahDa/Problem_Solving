# Quick sort
# takes an unsorted sequence and sorts it either in ascending or descending order
# start by taking unsorted sequence and choosing a pivot(number to base comparison of all numbers on)
# iterate through the rest of numbers in the list, comparing if its less or greater than the pivot
# less numbers go into one list and greater into one list, when its sorted lock it in
# do the whole process again, choosing an optimal pivot

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([4,5,4,6,3,4,8,8,5,12]))
print(quick_sort([4]))
