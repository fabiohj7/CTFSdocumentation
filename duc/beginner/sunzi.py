soldiers = 1000

while soldiers < 1100:
    if soldiers % 3 == 2 and soldiers % 5 == 4 and soldiers % 7 == 5:
        print(soldiers)
        break
    else:
        soldiers += 1
