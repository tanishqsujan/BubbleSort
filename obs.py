def bubbles(arr):
    n= len(arr)
    
    #Traverse through the array
    for i in range(n):
        swap= False
        
        for j in range(0, n-i-1):
            
            #Traverse the array from 0 to n-i-1
            #Swap if the element is greater than the nexxt element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swap= True
                
         #If no two elements were swapped in inner loop, then break
        if swap== False:
            break
        

arr= [10, 29, 38, 47, 56, 64, 73, 82, 91]
bubbles(arr)

print("Sorted Array: ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")  
                