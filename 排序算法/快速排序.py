# 快速排序使用分而治之来获得与归并排序相同的优点，而不使用额外的存储。
# 有可能列表不能被分成两半。当这种情况发生时，性能降低
# https://blog.csdn.net/u014745194/article/details/72783479


def quick_sort(alist, start, end):
    if start>= end:
        return
    #基准
    mark = alist[start]
    left = start
    right = end
    while left < right:
        while left<right  and alist[right]>mark:
            right-=1
        alist[left]=alist[right]
        while left<right and alist[left]<mark:
            left+=1
        alist[right]=alist[left]
    alist[right]=mark
    quick_sort(alist,start,left-1)
    quick_sort(alist,left+1,end)
alist=[54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)
