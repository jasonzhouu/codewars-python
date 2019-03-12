def row_sum_odd_numbers(n):
    start = int(n * (n-1) / 2)
    sum = 0
    i = 1
    while( i <= n ):
        sum += (start * 2 + 1)
        i += 1
        start += 1
    return sum

print(row_sum_odd_numbers(41))
