# 变换步长（增量）的插入排序->(n ~ n^2,不稳定)
def shell_sort(alist):
    gap=len(alist)//2
    while gap>=1:
        for i in range(gap,len(alist)):
            j=i
            while(j-gap)>=0:
                if alist[j]<alist[j-gap]:
                    alist[j],alist[j-gap]=alist[j-gap],alist[j]
                    j-=gap
                else:
                    break
        gap//=2
alist=[54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)

