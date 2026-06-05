cube = lambda x: x*x*x

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1]

    for _ in range(n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))