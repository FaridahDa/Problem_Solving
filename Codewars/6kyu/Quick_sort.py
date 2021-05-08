"""
There is an implementation of quicksort algorithm. Your task is to fix it. All inputs are correct.

"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    item_l = []
    item_g = []

    for x in arr:
        if x > pivot:
            item_g.append(x)
        else:
            item_l.append(x)

    return (quicksort(item_l) + [pivot] + quicksort(item_g))