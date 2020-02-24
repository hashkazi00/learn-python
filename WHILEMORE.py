secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
a=int(input("enter a number"))
while a!=secret_number:
    if a!=secret_number:
        print("HAHA!Stucked guys")
    else:
        print("You are free now")
    a=int(input("enter the secret number"))
print("YOU ARE FREE NOW")