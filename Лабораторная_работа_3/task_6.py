list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

m = min(list_numbers)
l = len(list_numbers)
for i in range(l):
    if list_numbers[i] > m:
        m = list_numbers[i]
        pos_max = i

temp = list_numbers[pos_max]
list_numbers[pos_max] = list_numbers[l-1]
list_numbers[l-1] = temp

print(list_numbers)
