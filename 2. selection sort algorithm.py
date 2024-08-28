def selection_sort(lst):
    for i in range(len(lst)-1):
        select = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[select]:
                select = j
        lst[i], lst[select] = lst[select], lst[i]
    return lst


n = 5
lst = [2, 6, 8, 4, 10]
print(selection_sort(lst))
