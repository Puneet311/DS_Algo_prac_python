def bubble_sort(arr_list):
    for i in range(len(arr_list)-1):
        for j in range(0,len(arr_list)-i-1):
            if(arr_list[j]>arr_list[j+1]):
                arr_list[j],arr_list[j+1]=arr_list[j+1],arr_list[j]
    return arr_list


arr_lis=[2,5,4,2,56,32,12]
print(bubble_sort(arr_lis))

arr_lis=[123,425,0,1,75,86,95]
print(bubble_sort(arr_lis))


#analysis of bubble sort.
#1- if data is sorted no. of passes=n-1
                        # no. of comparision in each pass=0  so time complexity is O(n)

#2 if data is reverse sorted   no of passes is n-1
#                       no. of comparision in each pass == (n-1)+(n-2)+(n-3)+......2+1=n(n+1)/2
#                           time complexity is O(n^2)
# 3- when data is in random order.
#                 no. of passes req.  p passes
#                   no. of comparision = (n-1)+(n-2)+(n-3)+.....(n-p)=(2pn-p^2-p)/2
#                   time complexity=O(n^2)                        
