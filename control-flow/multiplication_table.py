number = int(input("Enter a number to see its multiplication table: "))

for multiplier in range(1,11):
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")