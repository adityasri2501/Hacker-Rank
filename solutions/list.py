if __name__ == '__main__':
    N = int(input())
    l=list()
    for _ in range(N):
        cmd, *val = input().split() 
        val = list(map(int, val))
        if cmd == "print":
            print(l)
        elif cmd == "insert":
            l.insert(val[0], val[1])
        elif cmd == "remove":
            l.remove(val[0])
        elif cmd == "append":
            l.append(val)
        elif cmd == "sort":
            l.sort()
        elif cmd == "pop":
            l.pop()
        elif cmd == "reverse":
            l.reverse()

    #  the unpacking of inputs can also be done by
    # part = input().split()
    # cmd = part[0]
    # val = part[1:]