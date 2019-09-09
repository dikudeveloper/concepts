
def shortestSubstring(s):
    # Write your code here
    uniq = list(set(s))
    returner = []
    for i in range(0, len(s)):
        uniq_c = uniq.copy()
        x = ''
        for c in s[i:]:
            x += c
            if c in uniq_c:
                uniq_c.remove(c)
            if len(uniq_c) < 1:
                break
        if len(uniq_c) < 1:
            returner.append(x)
    lenth = list(map(len, returner))

    return min(lenth)
