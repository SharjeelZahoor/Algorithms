def binary_search_algo_sqrt(key):
    s = 0
    e = key
    mid = (s + e)//2
    ans = -1
    while s <= e:
        if key == mid * mid:
            return mid
        elif key < mid * mid:
            e = mid - 1
            ans = mid
        else:
           s = mid + 1
        mid = (s+e)//2
    return ans

key = int(input("Enter value for square root : "))
result = binary_search_algo_sqrt(key)
print(f" The square root of {key} is {result}")