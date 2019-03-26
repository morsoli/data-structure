#分而治之，递归分解/递归合并 （nlog）
def merge_sort(alist):
    if len(alist)<=1:
        return alist
    mid = len(alist)//2
    left_alist = merge_sort(alist[:mid])
    right_alist = merge_sort(alist[mid:])
    return merge(left_alist,right_alist)
def merge(left_list,right_list):
    result=[]
    j=0
    i=0
    while i<len(left_list) and j < len(right_list):
        if left_list[i]<=right_list[j]:
            result.append(left_list[i])
            i+=1
        else:
            result.append(right_list[j])
            j+=1
    result+=left_list[i:]
    result+=right_list[j:]
    return result
alist=[54,26,93,17,77,31,44,55,20]
print(merge_sort(alist))
        