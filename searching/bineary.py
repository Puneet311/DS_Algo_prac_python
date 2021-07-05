#binary searcg works only for sorted array

def binary_search(arr_lis,n,item_searched):
    start=0
    last=n-1
    while(start<last):
        mid=(start+last)//2
        if(arr_list[mid]==item_searched):
            return mid
        elif(arr_list[id]>item_searched):
                last=mid-1 
        elif(arr_list[mid]<item_searched):
            start=mid+1
    return -1

n=int(input("enter the size of array"))

arr_list=[int(input("enter the item of list")) for i in range(n)]
arr_list.sort()
print(arr_list)
item_searched=int(input("enter the item to be searched:"))

result=binary_search(arr_list,n,item_searched)

if(result==-1):
    print("item is not present in array")

else:
    print("item is present at index:",result)


    # Binar search analysis
    # 1- Best case-->when the searched item is present at the middle(i.e mid)  in that case the complexity is O(1)
    # 2- worst case -->when item is not present.
    # 3 for susseccful search-
    #  at start   item present are n
    # at 1st comparision  item present are n/2
    # at 2nd comparision item present are n/4
    # after 3rd    item present are n/8
    # after 4th comparision  item present are n/16
    # 
    # 
    # after ith comparision   item present are n/2^i
    # 
    # when item is searched   item present will be 1.
    # 
    # so no. of comparision required ===>  1=n/2^i  => 2^i=n => i=log(base2)n.  
    # Time complexity => o(log n)    

    # note -binary search can not be used on linked list