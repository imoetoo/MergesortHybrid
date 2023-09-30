import numpy as np
import time

comparison_count = 0
S = 20  # switch to insertion sort if array size smaller than S

def merge_sort(arr):
    global comparison_count

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparison_count = comparison_count+1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1


        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Insertion sort function
def insertion_sort(array):
    global comparison_count
    n = len(array)

    for i in range(1, n):
        j = i
        while j > 0:
            comparison_count += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
            j -= 1

    return array

def hybrid_sort(arr, s):
    if len(arr) <= 1:
        return arr  # Base case for recursion

    if len(arr) <= s:
        return insertion_sort(arr)

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = hybrid_sort(left_half, s)
    right_half = hybrid_sort(right_half, s)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    global comparison_count
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        comparison_count += 1
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged


comparison_count = 0
S = 20  # switch to insertion sort if array size smaller than S

def merge_sort(arr):
    global comparison_count

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparison_count = comparison_count+1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1


        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Insertion sort function
def insertion_sort(array):
    global comparison_count
    n = len(array)

    for i in range(1, n):
        j = i
        while j > 0:
            comparison_count += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
            j -= 1

    return array

def hybrid_sort(arr, s):
    if len(arr) <= 1:
        return arr  # Base case for recursion

    if len(arr) <= s:
        return insertion_sort(arr)

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = hybrid_sort(left_half, s)
    right_half = hybrid_sort(right_half, s)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    global comparison_count
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        comparison_count += 1
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged


#generating arrays of different sizes
# Create an array of 25 sizes, from 1000 to 10,000,000
sizes = np.linspace(1000, 10000000, 25).astype(int)
x = 10000000  # maximum value for each dataset

arrays = {}

for size in sizes:
    random_array = np.random.randint(1, x, int(size))  # Convert size to integer
    arrays[size] = random_array

random_array5000 = np.random.randint(1, x, 5000)
random_array100000 = np.random.randint(1, x, 100000)
arrays[5000] = random_array5000
arrays[100000] = random_array100000


print(arrays.keys())


# Fixing values of S, plot number of key comparisons over different sizes of the input list n. From results, when S increases, KC increases
def first_part():
    global comparison_count  # Use the global variable
    for keys in arrays.keys():
        comparison_count = 0  # Reset before each sort
        temp_dataset = arrays[keys].copy()
        hybrid_sort(temp_dataset, S)
        print("For datasize of ", keys)
        print("Number of comparisons:", comparison_count)

#Fix n (input list size) now, and run the key comparisons over a values of S. Number of key comparisons increases as size of input list S value increases
def second_part():
    global comparison_count  # Use the global variable
    global S  # Now S is also a global variable
    array_S = list(range(1, 51, 1))
    dataset = arrays[834250]
    for S in array_S:  # Change S here
        comparison_count = 0  # Reset before each sort
        temp_dataset = dataset.copy()
        hybrid_sort(temp_dataset, S)
        print("For S value of ", S)
        print("Number of comparisons:", comparison_count)

#Using different sizes of input datasets to determine an optimal value of S for the hybrid algorithm, which is 16
def third_part():
    global comparison_count  # Use the global variable
    global S  # Now S is also a global variable
    array_S = list(range(1, 51, 1))
    array_sizes = [1000, 417625, 2500750, 10000000]
    for i in range(4):
        for S in array_S:
            comparison_count = 0
            temp_dataset = arrays[array_sizes[i]].copy()
            hybrid_sort(temp_dataset, S)
            print("Dataset Size:", array_sizes[i])
            print("S value:", S)
            print("Number of comparisons:", comparison_count)

def fourth_part(): #same as above
    dataset = arrays[10000000]
    global comparison_count
    global S
    array_S = list(range(1, 51, 1))
    for S in array_S:
        comparison_count = 0
        temp_dataset = dataset.copy()
        hybrid_sort(temp_dataset, S)
        print("S value:", S)
        print("Number of comparisons:", comparison_count)

#after implementing the original version of Mergesort, compare its performance with hybrid algo for a dataset of 10 million integers, using S=16
def fifth_part_hybrid():
    dataset = arrays[10000000]
    global comparison_count
    global S
    S = 16
    temp_dataset = dataset.copy()
    comparison_count = 0
    start_time = time.time()
    hybrid_sort(temp_dataset, S)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"HybridSort Perfomance: KeyComparisons = {comparison_count}, Time taken = {elapsed_time}")

def fifth_part_merge():
    dataset = arrays[10000000]
    global comparison_count
    global S
    S = 16
    temp_dataset = dataset.copy()
    comparison_count = 0
    start_time = time.time()
    merge_sort(temp_dataset)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"MergeSort Perfomance: KeyComparisons = {comparison_count}, Time taken = {elapsed_time}")

fifth_part_merge()
fifth_part_hybrid()
