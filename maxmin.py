def find_min_max(array):
    max = array[0]
    min = array[0]
    for i in array[1:]:
        if i > max:
            max = i
        elif i < min:
            min = i
    return min, max

array = input("Enter a list of integers separated by spaces: ")
array = [int(i) for i in array.split()]
min, max = find_min_max(array)

print(f'Minimum: {min}\nMaximum: {max}')
