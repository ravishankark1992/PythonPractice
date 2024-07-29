# Function to find the first occurrence of an element in a
# sorted array
def firstOcc(arr, l, h, x):
    if h >= l:
        mid = (l + h) // 2

        # Check if the element is present at the middle or
        # if the element is present in the left half (if
        # the element is greater than the middle element)
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            # Search in the right half
            return firstOcc(arr, mid + 1, h, x)
        else:
            # Search in the left half
            return firstOcc(arr, l, mid - 1, x)
    return -1

# Function to find the last occurrence of an element in a
# sorted array
def lastOcc(arr, n, l, h, x):
    if h >= l:
        mid = (l + h) // 2

        # Check if the element is present at the middle or
        # if the element is present in the right half (if
        # the element is smaller than the middle element)
        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            # Search in the left half
            return lastOcc(arr, n, l, mid - 1, x)
        else:
            # Search in the right half
            return lastOcc(arr, n, mid + 1, h, x)
    return -1

# Function to count the occurrences of an element in a
# sorted array
def countOccurrences(arr, n, x):
    # Find the first and last occurrences of the element
    idxFirst = firstOcc(arr, 0, n - 1, x)

    # If the element does not exist, return -1
    if idxFirst == -1:
        return -1
    idxLast = lastOcc(arr, n, idxFirst, n - 1, x)

    # Return the difference between the last and first
    # occurrences + 1 to get the total count
    return idxLast - idxFirst + 1

if __name__ == "__main__":
    arr = [2, 2, 2, 2, 3,4,5,7]
    n = len(arr)
    x = 2

    occurrences = countOccurrences(arr, n, x)

    print("Number of occurrences of", x, ":", occurrences)