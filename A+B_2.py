while True:
    try:
        n = int(input())
        for i in range(n):
            line = input().split(' ')
            a, b = int(line[0]), int(line[1])
            print(a + b)
    except EOFError:
        break
