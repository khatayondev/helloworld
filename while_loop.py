def evens():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    if x > y:
        x, y = y, x
    current = x if x % 2 == 0 else x + 1
    while current <= y:
        print(current)
        current += 2

evens()