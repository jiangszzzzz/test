while True:
    try:
        a, b = int(input()), 0
        if a > 0:
            if a == 1 or a == 2:
                b = -1
            elif a % 2 == 1:
                b = 2
            elif a % 4 == 0:
                b = 3
            else:
                b = 4
            print(b)
    except:
        break