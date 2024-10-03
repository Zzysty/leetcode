while True:
    try:
        a,b = input().split(' ')
        print(int(a)+int(b), end="\n\n")
    except EOFError:
        break
