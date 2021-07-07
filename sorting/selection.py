#selction sort is type of in-place sort(no need of extra space).
# basic idea is to find the smallest item from array and keeping it at its proper position

def selection_sort(arr_list):
    for i in range(len(arr_list)-1):
        minIndex=i  # to find the min index of smallest element.
        for j in range(i+1,len(arr_list)):
            if(arr_list[j]<arr_list[minIndex]):
                minIndex=j
        if(i!=minIndex):
            arr_list[i],arr_list[minIndex]=arr_list[minIndex],arr_list[i]

lis=[2,3,4,5,2,7,6]
selection_sort(lis)
print(lis)   

lis1=[2,45,12,53,64,89,75,123]
selection_sort(lis1)
print(lis1)

lis2=[4]
selection_sort(lis2)
print(lis2)


######################

# pass 1: arr[minIndex] is compared with the arr[1].....ar[n-1]  --> n-1 comparison
#pass2 : arr[minIndex] is compared with arr[2]..........arr[n-1] --> n-2 comparion
# pass3                                                            --> n-3 comparion
#
#
#pass n-1: arr[minIndex] is compared with a[n-1] --> 1 comparision
#    total comparision== n(n-1)/2  time complexity-- O (n^2).
