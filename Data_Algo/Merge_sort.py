# merge sort is a divide and conquer algorithm, it involves breaking down a breakdown a problem into smaller problems
# recursively until they become a easier solution solutions are combined to solve the original problem
# split array in half, call merge sort on each half recursively, merge both sorted halves into one sorted array


def merge_sort(array):
    if len(array) <= 1: return array
    midpoint = int(len(array) / 2)  # divide the array by 2 to get the midpoint

    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])  # splitting the list
    return merge(left, right)


def merge(left,right):

    result = []
    right_pointer = left_pointer = 0 #setting the index

    while left_pointer < len(left) and right_pointer < len(right): #basically saying while there are elements in both arrays
        #if the element at left pointer(index 0) in the left array is less than index 0 in the right array then send results to empty list
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1 #incrementing the index so it goes through all the indexes in the list

        else:
            result.append(right[right_pointer])
            right_pointer +=1

#if the while loop doesnt trigger, then to cheat we can do extend.. taking everything everything from index zero and returning to the end
    result.extend(left[left_pointer:]) #if the while element isn't true then we use this to work around
    result.extend(right[right_pointer:])

    return result # return resulting array


def main():
    array = [9,3,4,5,6]
    print(array)

    result = merge_sort(array)
    print(result)


if __name__ == "__main__":
    main()


