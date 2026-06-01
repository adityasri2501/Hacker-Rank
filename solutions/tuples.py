if __name__ == '__main__':
    n = int(input())
    integer = tuple(map(int, input().split()))
    print(hash(integer))

# the hash values changes as per the local machine and server