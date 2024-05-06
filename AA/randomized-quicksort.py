import random

def get_partition_random(array, low, high):
    pivot_index = random.randint(low, high)  
    pivot = array[pivot_index]
    swaps = 0
    i = low
    for j in range(low, high + 1):
        if j != pivot_index and array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            swaps += 1
    return i - 1, swaps

def get_partition_leftmost(array, low, high):
    pivot = array[low]  # Choose leftmost element as the pivot
    swaps = 0
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            swaps += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    swaps += 1
    return i - 1, swaps

def quicksort_random(array, low, high):
    if low < high:
        partition, swaps = get_partition_random(array, low, high)
        quicksort_random(array, low, partition - 1)
        quicksort_random(array, partition + 1, high)
        return swaps

def quicksort_leftmost(array, low, high):
    if low < high:
        partition, swaps = get_partition_leftmost(array, low, high)
        quicksort_leftmost(array, low, partition - 1)
        quicksort_leftmost(array, partition + 1, high)
        return swaps

array = [4, 1, 3, 5, 6]
array_copy = array[:]  
swaps_random = quicksort_random(array, 0, len(array) - 1)
swaps_leftmost = quicksort_leftmost(array_copy, 0, len(array_copy) - 1)

print("Number of swaps with random pivot:", swaps_random)
print("Number of swaps with leftmost pivot:", swaps_leftmost)
