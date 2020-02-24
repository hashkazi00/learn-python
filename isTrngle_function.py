def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
    
print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))