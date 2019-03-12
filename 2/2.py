def max(input_array):
    input_array.sort()
    return input_array[-1]

def min(input_array):
    input_array.sort()
    return input_array[0]

x = [1, 2, -1, 10]
print(max(x))
print(min(x))
