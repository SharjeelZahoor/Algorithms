def bubble_sort(lst):
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst


lst = [2,4,1,6,5,3]
n = len(lst)
print(bubble_sort(lst))