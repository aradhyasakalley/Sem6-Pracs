import random
swaps_randomized = 0
swaps_regular = 0

# Regular partition functions just keeping track of randomized count
# Written separately only to have diff count 
def partition_random(arr,low,high):
    global swaps_randomized
    i = low
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            swaps_randomized += 1
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    swaps_randomized += 1
    arr[i],arr[high] = arr[high],arr[i]
    return i 

def partition_regular(arr,low,high):
    global swaps_regular
    i = low
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            swaps_regular += 1
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    swaps_regular += 1
    arr[i],arr[high] = arr[high],arr[i]
    return i 


def partition_randomizer(arr,low,high):
    r = random.randint(low,high)
    arr[r],arr[high] = arr[high],arr[r]
    return partition_random(arr,low,high)

# Same quicksort main functions except the random one calls the randomizer first while the regular one calls the partition function direct;y
def quicksort_random(arr,low,high):
    if low < high:
        p = partition_randomizer(arr,low,high)
        quicksort_random(arr,low,p-1)
        quicksort_random(arr,p+1,high)
        
def quicksort_regular(arr,low,high):
    if low < high:
        p = partition_regular(arr,low,high)
        quicksort_regular(arr,low,p-1)
        quicksort_regular(arr,p+1,high)


arr = [random.randint(1,100) for _ in range(100)]

print(arr)

quicksort_random(arr,0,len(arr)-1)
# print(arr,swaps_randomized)

quicksort_regular(arr,0,len(arr)-1)
# print(arr,swaps_regular)

print(f'Swaps using random approach are {swaps_randomized} while using regular approach is {swaps_regular} ')