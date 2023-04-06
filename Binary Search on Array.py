n,k=map(int,input().split())
arr=list(map(int,input().split()))
l=0
r=n-1
def binarysearch(arr,l,h,k):
    if h>=l:
        mid=l+(h-l)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return binarysearch(arr,l,mid-1,k)
        else:
            return binarysearch(arr,mid+1,h,k)
    else:
        return -1
result=binarysearch(arr,0,n-1,k)

if result!=-1:
    print("true")
else:
    print("false")

