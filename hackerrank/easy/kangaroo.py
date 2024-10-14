def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    if (x2 - x1) % (v1 - v2) == 0 and (x1 - x2) * (v1 - v2) < 0:
        return "YES"
    return "NO"
