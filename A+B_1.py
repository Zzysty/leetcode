while True:
    try:
        s = input().split()
        a, b = int(s[0]), int(s[1])
        print(a + b)
    except EOFError:
        break
