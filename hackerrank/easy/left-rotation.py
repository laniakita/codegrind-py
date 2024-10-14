
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateLeft(d, arr):
    n = len(arr)
    d %= n
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    print(arr)

def rotateLeft2(d, arr):
    n = len(arr)
    dx = dx % n
    return arr[dx:] + arr[:dx]

rotateLeft(2, [1,2,3,4,5])
