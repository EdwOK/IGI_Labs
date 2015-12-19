def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array

    less = []
    more = []
    pivot_list = []

    pivot = array[n / 2]
    for i in array:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            pivot_list.append(i)

    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivot_list + more


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array

    left = array[:n / 2]
    right = array[n / 2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(array1, array2):
    merged_array = []

    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())

    merged_array.reverse()
    return merged_array
