# insertion sort is basically inspired by the card player, take a number and insert that number to its proper place in sorted list.

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr

arr_list=[2,5,1,80,9]
print(insertion_sort(arr_list)) 

arr_list2=[2,45,1,0,-3,-80,56,4,0,89]
print(insertion_sort(arr_list2))


#when array is in sorted order
# time complexity is O(N)

#when arr is in reverse sorted order
# time complexity is O(n^2)

#when arr is in random order.

