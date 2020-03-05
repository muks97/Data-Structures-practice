

def find_closest(a, target):
    min_diff =float("inf")
    low =0
    high =len(a)-1
    #min_diff=0
    closest_num= None
    if len(a)==0:
        return None
    if len(a)==1:
        return a[0]
    while low<=high:
        mid = (low+high) //2
        if mid+1<len(a):
            min_diff_right= abs(a[mid+1]-target)
        if mid>0:
            min_diff_left=abs(a[mid-1]-target)
        
        if min_diff_left< min_diff:
            min_diff=min_diff_left
            closest_num=a[mid-1]
        if min_diff_right<min_diff:
            min_diff=min_diff_right
            closest_num=a[mid+1]
        

        if a[mid]<target:
            low = mid+1
        elif a[mid]>target:
            high = mid-1 
        else:
            return a[mid]  
        

    return closest_num

A=[1, 2, 3, 5, 6, 6 ,7 ,8 , 9]
print(find_closest(A, 4))

