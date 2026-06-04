def formatted(n):
    width = len(bin(n))-2 # max width of one column
    for i in range(1,n+1):
        print(f"{i:>{width}}{oct(i)[2:]:>{width}}{hex(i)[2:]:>{width}}{bin(i)[2:]:>{width}}") 
        # or
        # print(f"{i:{width}d} {oct(i)[2:]:>{width}} {hex(i)[2:]:>{width}} {bin(i)[2:]:>{width}}")
        # output is like this 17 0o21 0x11 0b10001
        # that is why sliced from 2nd index to last
        # :>{width} = right aligned
        # :<{width} = left aligned
        # :^{width} = center aligned

if __name__ == '__main__':
    n = int(input())
    formatted(n)