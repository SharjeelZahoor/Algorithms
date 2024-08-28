def first_occ(lst, key):
    start = 0
    end = len(lst)-1
    middle = (start + end) // 2
    ans = 0
    while start <= end:
        if lst[middle] == key:
            ans = middle
            end = middle - 1
        elif lst[middle] < key:
            start = middle + 1
        elif lst[middle] > key:
            end = middle - 1
        middle = (start + end)//2
    return ans


def last_occ(lst, key):
    start = 0
    end = len(lst)-1
    ans = 0
    middle = (start + end) // 2
    while start <= end:
        if lst[middle] == key:
            ans = middle
            start = middle + 1
        elif lst[middle] < key:
            start = middle + 1
        elif lst[middle] > key:
            end = middle - 1
        middle = (start+end)//2
    return ans


lst = sorted(list(map(int, input().split())))
print(lst)
key = int(input())
result = first_occ(lst, key)
print(f"first occurrence of {key} is at index : {result}")
result = last_occ(lst, key)
print(f"Last occurrence of {key} is at index : {result}")