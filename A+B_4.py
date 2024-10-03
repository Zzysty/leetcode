while True:
    try:
        line = input().split()
        if line[0] == '0':
            break
        m = map(lambda x: int(x), line[1:])
        l = list(m)
        s = sum(l)
        print(s)
    except EOFError:
        break
