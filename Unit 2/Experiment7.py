def insert(arr, pos, value):
    shifts = 0
    n = len(arr)
    
    arr.append(0)  
    
    
    for i in range(n, pos, -1):
        arr[i] = arr[i-1]
        shifts += 1
    
    arr[pos] = value
    return arr, shifts


def delete(arr, pos):
    shifts = 0
    n = len(arr)
    
    
    for i in range(pos, n-1):
        arr[i] = arr[i+1]
        shifts += 1
    
    arr.pop()
    return arr, shifts 




arr = [10, 20, 30, 40, 50]


print("Insertion:")
new_arr, shift_count = insert(arr.copy(), 2, 25)
print("Updated Array:", new_arr)
print("Shift Count:", shift_count) 


print("\nDeletion:")
new_arr, shift_count = delete(arr.copy(), 1)
print("Updated Array:", new_arr)
print("Shift Count:", shift_count) 