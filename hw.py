def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Taking user input for the array
arr = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)

bubble_sort(arr)

print("Sorted Array:")
print(" ".join(map(str, arr)))
