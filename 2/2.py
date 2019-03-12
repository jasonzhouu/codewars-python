def max(input_array):
    max = input_array[0]
    for i in input_array:
        if i > max:
            max = i
    return max

def min(input_array):
    min = input_array[0]
    for i in input_array:
        if i < min:
            min = i
    return min

x = [1, 2]
print(max(x))
print(min(x))
