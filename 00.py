def Merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left=left+1
        else:
            temp.append(arr[right])
            right=right+1

    while left<=mid:
        temp.append(arr[left])
        left=left+1
    while right<=high:
        temp.append(arr[right])
        right=right+1

    for i in range(len(temp)):
        arr[low+i]=temp[i]
    return arr

    return temp
def Divide(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    Divide(arr,low,mid)             #this is left Half
    Divide(arr,mid+1,high)          #this is Right Half
    x=Merge(arr,low,mid,high)
    return x

arr=[3,4,56,234,63,123,656,231,435,12,54,67,21,123,4]
low=0
high=len(arr)-1
print(Divide(arr,low,high))

