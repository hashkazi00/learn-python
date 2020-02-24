rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)
vacancy=0
for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy+=1
print(vacancy)