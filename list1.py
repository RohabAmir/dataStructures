# my_list[1,2,4,5,10,6,3]  A list having integers 
# my_list=[1,5,3] After removing even integer 
# SOL:1 Simple Method

def removeEven(list):
    odds=[] #Creating a new empty list
    for number in list: # Iterate over input list
        if number%2 !=0: #Checks if the number is NotEVen
            odds.append(number) #Appending the number in the new empty list
    return odds
print(removeEven([1,22,3,5,10,6,3]))

# SOL:2 #Using List Comprehension method

def removeEven(list):
    return[number for number in list if number%2 !=0] #List Comprehension to iter over and add to a new list(if not even)
print(removeEven([3,2,44,3,34]))

