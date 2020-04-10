i = 0
numbers = []

# Range(start=1, end, increment)
for i in range(1, 6, 1):
    print(f"At the top i is {i}")
    numbers.append(i)

    print("Numbers now: ", numbers)
    # This is a superficial way of ensuring the same output text
    # as we didn't increment the i value manually – it is iterated
    print(f"At the bottom i is {i + 1}")
    # Again, this continuity only works when increment is set to 1.


print("The numbers: ")

for num in numbers:
    print(num)

# Study Drill 5: Converted ex31.1.py to use for loops and range

# Recall: "range(start, stop[, step])" -pydoc
# –> Range takes an optional step/increment integer value;
# therefore an "increment" variable is not necesary.
