def binary_search(arr, search_value):
    """
    This function implements binary search algorithm to find a specific element in a sorted list.
    The function takes three parameters: a sorted list, the target element to search for, and the index of the first element in the list.
    The function returns the index of the target element if found, or -1 if it is not present in the list.
    """
    # Your implementation here
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid= int((start + end)/2)
        print(arr[mid])
        if arr[mid] == search_value:
            return mid
        else:
            if arr[mid]>=search_value:
                end = mid - 1
            else:
                start = mid + 1
    return -1
def binary_search_recursive(arr, l, r, search_value):
    while l<=r:
        mid = int((l+r)/2)
        if arr[mid] == search_value: 
            return mid
        elif arr[mid]<search_value:
            l = mid + 1
            return binary_search_recursive(arr, l, r, search_value)
        else:
            r = mid - 1
            return binary_search_recursive(arr, l, r, search_value)
        
    return -1


# Test the function
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr=[3,6,8,12,14,17,25,29, 31,36,42,47,53,55,62]
search_value = 44
index = binary_search_recursive(arr,0,len(arr)-1, search_value)
#index = binary_search(arr, search_value)
if index == -1:
    print(search_value, "not found")
else:
    print("found",index,arr[index])