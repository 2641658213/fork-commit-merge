def bubble_sort(arr):
    # TODO: Implement the bubble sort algorithm

    # Get the length of the array
    n = len(arr)

#! Test cases (Don't edit):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
