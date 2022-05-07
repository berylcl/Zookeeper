numbers = [2, 4,4, 5, 5, 78, 8, 9]
uniques = []
for item in numbers:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)