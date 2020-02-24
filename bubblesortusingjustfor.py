myList = [1, 6, 10, 3, 4] # list to sort

for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up here it means that we have to swap the elements

for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up her
        
for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up here it means that we have to swap the elements

for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up her
        
print(myList)