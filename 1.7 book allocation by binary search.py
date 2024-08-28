def binary_search_algo(lst,n,student):
    s = 0
    sum = 0
    for i in range(n):
        sum += lst[i]
    e = sum
    ans = -1
    mid = s + (e-s)//2
    while (s<=e):
        if (ispossible(lst,n,student,mid)):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
        mid = s + (e - s)//2
    return ans

def ispossible(lst,n,student,mid):
    studentCount = 1
    pagesum = 0

    for i in range(n):
        if pagesum+lst[i] <= mid:
            pagesum+= lst[i]
        else:
            studentCount+=1
            if(studentCount > student or lst[i] > mid):
                return False
    return True



n = 4 
student = 2
lst = [10,20,30,40]
print(binary_search_algo(lst,n,student))


