def fizzbuzz(number):
    if number % 15 == 0:
        return print("Fizzbuzz")
    elif number % 3 == 0:
        return print("Fizz")
    elif number % 5 == 0:
        return print("Buzz")
    return False


def main():
    for i in range(1, 101):
        if fizzbuzz(i) is False:
            print(i)
    return

if __name__ == '__main__':
    main()
