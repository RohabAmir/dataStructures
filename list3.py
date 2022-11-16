# Find two numbers that add up to "k"
#Sol;1

def findSum(lst,k):
    for i in range(len(lst)): #Using nested for loops each iterating over the entire list
        for j in range(len(lst)):
    #If sum of both iterators is k and i is not equal to j this will serve the purpose
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i],lst[j]]
print(findSum([1,2,3,4],7))

#Sol;2

def findSum(lst,k):
    lst.sort() # sort the given list
    index1=0 # this is at the first index of given list
    index2=len(lst)-1 # this is pointing at the last index
    result=[] #Creating a new list
    sum=0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while(index1 != index2):
        sum=lst[index1]+lst[index2]
        if sum<k:
            index1+=1
        elif sum>k:
            index2-=1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False
print(findSum([4,2,3,1],7))
print(findSum([1,2,3,4],2))


