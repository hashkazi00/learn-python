myList = [22, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 22
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")