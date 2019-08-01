def foo(k):
    k[0] = 1


if __name__ == '__main__':
    q = [0]
    foo(q)
    print(q)

# What's the output of the following piece of Code?
# a) [0].
# b) [1].
# c) [1, 0].
# d) [0, 1].
