# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#
from math import ceil


def minSum(num, k):
    # Write your code here
    if len(num) == 1:
        num[0] = ceil(num[0] / (2 * k))
        return num[0]
    else:
        counter = 1
        while counter <= k and len(num) <= 10 ** 5 and k <= 10 ** 7:
            i = max(num)
            position_i = num.index(i)
            j = ceil(i / 2)
            num[position_i] = j
            counter += 1
        return sum(num)


def minSum(num, k):
    # Write your solution here
    if (len(num) >=1 and len(num) <= 10**5) and (k>=1 and k<=10**7) and (0 not in num):
        counter = 1
        while counter <= k:
            max_value = max(num)
            new_value = ceil(max_value / 2)
            num[num.index(max_value)] = new_value
            counter += 1
        return sum(num)
