numbers = []


for i in range(10):
    value = int(input("Enter a number: "))
    numbers.append(value)


largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num


print("The largest number is:", largest)
