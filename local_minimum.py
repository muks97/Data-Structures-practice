a= [3, 5, 2, 0, 7, 1, 8]

def peakIndexInMountainArray(A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return a[lo]

        

print(peakIndexInMountainArray(a))
    