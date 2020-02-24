largest_num = -999999
counter = 0

while True:
    number=int(input("enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter+=1
    if number>largest_num:
        largest_num=number

if counter !=0:
    print("the largest number is",largest_num)
else:
    print("you havent entered")