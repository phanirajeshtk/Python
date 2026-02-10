# Linear Search
arr = [5,6,7,8,9]
pos = -1
x= int(input("enter the number for search"))

def search(arr, x):
    for j in range(len(arr)):
        if(arr[j]) == x:
            globals()["pos"] = j
            return True

    return False

if search(arr, x):
    print("found at position",pos)
else:
    print("not found")

