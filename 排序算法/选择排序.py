def select_sort(alist):
    for i in range(len(alist)-1):
        min_index=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[min_index]:
                min_index=j
        if i!=min_index:
            alist[i],alist[min_index]=alist[min_index],alist[i]
alist=[54,26,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)