# binary search algorithm

def binary_search_algo(lst, key):
    start = 0
    end = len(lst) -1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] == key:
            return middle
        elif lst[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return -1


lst = [2,4,6,8,10,12,14]
key = 12
result = binary_search_algo(lst, key)
print(result)