def fibonacci(n):
    """Naive Recursive Algorithm"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_optimized(n):
    """Memoized Dynamic Programming Algorithm -- Top Down design"""
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_optimized(n-1) + fibonacci_optimized(n-2)
    return memo[n]


def fibonacci_bottom_up(n):
    """Bottom-Up Dynamic Programming Algorithm using Iteration"""
    for i in range(0, n+1):
        if i <= 1:
            f = i
        else:
            f = bottom_up_table[i-1] + bottom_up_table[i-2]
        bottom_up_table[i] = f
    return bottom_up_table[n]


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial_optimized(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = 1
    else:
        memo[n] = n * factorial_optimized(n - 1)
    return memo[n]


if __name__ == '__main__':
    import time
    memo = {}
    bottom_up_table = {}

    start = time.time()
    fib = fibonacci_optimized(40)
    end = time.time()
    time_delta = end - start
    print(fib, 'fibonacci_optimized(n) executed in {} seconds'.format(time_delta))

    start = time.time()
    fib = fibonacci_bottom_up(40)
    end = time.time()
    time_delta = end - start
    print(fib, 'fibonacci_bottom_up(n) executed in {} seconds'.format(time_delta))

    start = time.time()
    fib = fibonacci(40)
    end = time.time()
    time_delta = end - start
    print(fib, 'fibonacci(n) executed in {} seconds'.format(time_delta))

    # start = time.time()
    # fact = factorial_optimized(995)
    # end = time.time()
    # time_delta = end - start
    # print('factorial_optimized(n) executed in {} seconds'.format(time_delta))
    #
    # start = time.time()
    # fact = factorial(995)
    # end = time.time()
    # time_delta = end - start
    # print('factorial(n) executed in {} seconds'.format(time_delta))
