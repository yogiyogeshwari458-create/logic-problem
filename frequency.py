arr = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Element Frequency:")

for element, count in frequency.items():
    print(element, ":", count)