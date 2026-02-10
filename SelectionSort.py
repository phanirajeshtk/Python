#SelectionSort
arr = [10,6,4,5,9,2,6]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
         temp = arr[j]
         arr[j] = arr[j+1]
         arr[j+1] = temp
    print(arr)







