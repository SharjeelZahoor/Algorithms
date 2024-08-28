# finding the largest possible distance between the aggressive cows
def aggressive_cows(lst, k):
    s = 0
    e = max(lst) - min(lst)
    mid = s + (e-s) // 2

    ans = -1
    while(s<=e):
        if ispossible(lst, k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
        mid = s + (e - s)//2
    return ans

def ispossible(lst, k, mid):
    count = 1
    place = lst[0]
    for i in range(1,len(lst)):
        if lst[i] - place >= mid:
            count+=1
            if count == k:
                return True
            place = lst[i]
    return False


k = 2
l = [4, 2, 1, 3, 6]
lst = sorted(l)
print(f"maximum distance between {k} aggressive cows is  {aggressive_cows(lst, k)}")
