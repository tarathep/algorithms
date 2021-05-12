def binarySearch(arr,l,r,x):
    while l <= r:
        mid = l + (r - l)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [2,3,4,40,11]
x = 40

res = binarySearch(arr,0,len(arr)-1,x)
if res != -1:
    print("element is present at index % d" % res)
else:
    print("element is not present in array")