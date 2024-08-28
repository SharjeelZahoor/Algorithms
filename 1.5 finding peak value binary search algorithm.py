def mountain_list_peak_value(lst):
    start = 0
    end = len(lst)-1
    middle = (start + end)//2
    while start < end:
        if lst[middle] < lst[middle+1]:
            start = middle+1
        else:
            end = middle
        middle = (start+end)//2
    return lst[start]

lst = [1,3,4,5,6,23,76,22,12,4,2,1]
result = mountain_list_peak_value(lst)
print(result)

