def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    count = 0
    coverMax = 0
    idealCenter = 0
    actualCenter = 0

    for i in range(len(x)):
        if x[i] <= idealCenter:
            actualCenter = x[i]
            coverMax = actualCenter + k
            continue
        elif x[i] <= coverMax:
            continue
        else:
            count += 1
            idealCenter = x[i] + k
            actualCenter = x[i]
            coverMax = idealCenter
    return count
