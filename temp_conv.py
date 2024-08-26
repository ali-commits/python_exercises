def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():
    print("Choose conversion direction: ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        temp = float(input("Enter the temperature in celsius "))
        print(celsius_to_fahrenheit(temp))

    elif option == "2":
        temp = float(input("Enter the temperature in fahrenheit "))
        print(fahrenheit_to_celsius(temp))
    else:
        print("wrong option")


temperature_converter()
