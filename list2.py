#Sorting & Merging two lists into a new list 
def mergeList(lst1,lst2):
    result=[] #Creating a new result list
    #Creating three variables and assigning them to zero these are tracking the current index of the three lists
    index_arr1=0
    index_arr2=0
    index_result=0
    for i in range(len(lst1)+len(lst2)): #Traverse both the lists and insert smaller value value from arr1 or arr2 into resulted list and after that increment that lists index
        result.append(i)
    while(index_arr1 < len(lst1) and index_arr2 < len(lst2) ): 
        if(lst1[index_arr1] < lst2[index_arr2]):#Comaparing to get the smaller value
            result[index_result]= lst1[index_arr1]
            index_arr1 +=1     #Increamenting the indexes 
            index_result +=1 
        else:
            if(lst1[index_arr1] > lst2[index_arr2]):#Comaparing to get the smaller value
                result[index_result]= lst2[index_arr2]
                index_arr2 +=1     #Increamenting the indexes 
                index_result +=1 
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while(index_arr1 < len(lst1)):
        result[index_result]= lst1[index_arr1]
        index_arr1 +=1    
        index_result +=1 
    while(index_arr2 < len(lst2)):
        result[index_result]= lst2[index_arr2]
        index_arr2 +=1    
        index_result +=1 
    return result

print(mergeList([4,5,6],[-2,-1,0,7]))


#Merging two sorted list in one place i.e no new list is created 

def merge_List(lst1,lst2):
    ind1=0 #current indexex of both lists 
    ind2=0
    while ind1 < len(lst1) and ind2 < len(lst2):
        if(lst1[ind1]>lst2[ind2]):
             # insert list2's current index to list1
            lst1.insert(ind1,lst2[ind2]) #Insert(index,value)
            ind1 +=1
            ind2 +=1
        else: # if already the value in list1 is small the only increament it 
            ind1 +=1
    if ind2 < len(lst2): # if there are still elements left in the second list
        lst1.extend(lst2[ind2:])
    return lst1
print(merge_List([4,5,6],[-2,-1,0,7]))
