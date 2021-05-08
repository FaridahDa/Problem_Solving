# Conceptually, a merge sort works as follows :
# Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
# Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

# Write a Python program to sort a list of elements using the merge sort algorithm.


def merge_sort(array):
    if len(array) <= 1: return array
    midpoint = int(len(array) / 2)
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    right_pointer = left_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer +=1
        else:
            result.append(right[right_pointer])
            right_pointer +=1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


def main():
    array = [3, 5, 7, 9, 0, 8, 2]
    print(array)

    result = merge_sort(array)
    print(result)

if __name__ == "__main__":
    main()



