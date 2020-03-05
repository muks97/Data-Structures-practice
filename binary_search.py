data=[1,2,3,4,5,6,7,32,2,35,7,8,4]
target =5


def binary_search(data, target):
    low=0
    high =len(data)-1

    while low<=high:
        mid = (low+high)//2
        if data[mid]==target:
            return True
        elif target< data[mid]:
              high = mid-1
        else: 
              low =mid+1
    return False

print(binary_search(data, target))