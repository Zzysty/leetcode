while True:
    try:
        n = int(input())
        for i in range(n):
            line = input().split(' ')
            if line[0] == '0':
                break
            # m = map(lambda x: int(x), line[1:])
            l = [int(x) for x in line[1:]]
            s = sum(l)
            print(s, end="\n\n")
            if i != n - 1:
                print()
    except EOFError:
        break
