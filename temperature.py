MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main ():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit(celcius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit : "))
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            celsius = get_celcius
            # Remove the "pass" statement when you are done. It's a placeholder.
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")a
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_fahrenheit(celcius):
    fahrenheit = celsius * 9.0 / 5 + 32
def get_celcius(fahrenheit):
    celcius = 5 / 9 * (fahrenheit - 32)