largest_number=-9999999999
a=int(input("enter a number or enter -1 to exit"))

while a!=-1:
    if a>largest_number:
        largest_number=a
    else:
        a=int(input("enter the lrgest no."))

print("the largest no is:",largest_number)