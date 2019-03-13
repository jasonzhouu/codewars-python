def maxSequence(arr):
    largest_sum = 0
    for array_length in range(1, len(arr)+1):
        for start_index in range(0, len(arr)-array_length+1):
            sum_temp = sum(arr[start_index:(start_index+array_length)])
            if sum_temp > largest_sum:
                largest_sum = sum_temp
    return largest_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSequence(arr))
