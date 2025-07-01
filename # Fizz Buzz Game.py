# Fizz Buzz Game

cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
for hodnota in cisla:
    if hodnota % 5 and hodnota % 3:
        print("FizzBuzz")
    elif hodnota % 3:
        print("Fizz")
    elif hodnota % 5:
        print("Buzz")
    else:
        print(hodnota)
