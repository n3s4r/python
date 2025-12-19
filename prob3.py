list1 = [6, 9, 9, 6, 96, 69, 69.69, 96.69, "sixty nine", "ninety six"]
list2 = []

for item in list1:
    if isinstance(item, int):
        list2.append(item)

list2.sort()

print("Original list:", list1)
print("Modified list:", list2)