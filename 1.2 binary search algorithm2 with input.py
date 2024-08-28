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


print("Enter your space separated list")
lst = sorted(list(map(int, input().split())))
sortlist = lst
print(sortlist)
key = int(input("enter your key : "))
result = binary_search_algo(lst, key)
print(result)