if __name__ == '__main__':
    arr = set(map(int, input().split()))
    arr = list(arr)
    sorted(arr)
    if len(arr)>=2:
        print(arr[-2])
    else:
        print("No runner up score")