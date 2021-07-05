def linear_search(lis,n,item_searched):
    for i in range(n):
        if(lis[i]==item_searched):
            return i
    return -1

#searching an item.

n=int(input("enter the array length"))
arr_lis=[int(input("enter the integer value-"+str(i)+":")) for i in range(n)] 
item_searched=int(input("enter the item to be searched"))
result=linear_search(arr_lis,n,item_searched)

if(result==-1):
    print("item not found")
else:
    print("item is found at:",result)   
    

#analysis of linear search.
#best case of linear search--

# -if item is present at position 1---> 1 comparision is needed--->time complexity  O(1)

# --worst case
# if item is present at last position--> n comparision are needed -->tiome complexity O(n)

#average case

# if item is present at ith position -->i comparision are needed
#  Average no. of comparision needed for successful search-->

#   (1+2+3+4+5.......+n)/n=(n+1)/2  time complextiy for average case is --O(n)