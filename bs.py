def bubblesort(arr):
    n= len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                
                
                
arr= [64, 35, 23, 58, 91, 44, 79, 86]
bubblesort(arr)

print("Sorted Array: ")
for i in range(len(arr)):
    print("%d" %arr[i], end= " ")