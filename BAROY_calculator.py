def main():

    print("===== BASIC TECHNICAL CALCULATOR =====")
    print("1. Basic Math (Add/Subtract/Multiply/Divide)")
    print("2. Percentage Calculator")
    print("3. Area & Perimeter (Square/Rectangle/Circle)")
    print("4. Temperature Converter")
    print("5. Exit")

    while True:

        choice = input("\nChoose an option(1-5): ")

        if choice == '1':
            # Basic Math Operations
            print("\n--- BASIC MATH ---")
            num1 = float(input("x: "))
            num2 = float(input("y: "))
            op = input("Operation (+, -, *, /): ")

            if op == '+':
                print(f"Result: {num1 + num2}")
            elif op == '-':
                print(f"Result: {num1 - num2}")
            elif op == '*':
                print(f"Result: {num1 * num2}")
            elif op == '/':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Math ERROR!")
            else:
                print("The operation chosen is not correct!")

        elif choice == '2':
            # Percentage Calculator
            print("\n--- PERCENTAGE CALCULATOR ---")
            base_num = float(input("Base number (e.g., 100): "))
            percent = float(input("Percentage you want to get(e.g., 25): "))
            result = (percent / 100) * base_num
            print(f"{percent}% of {base_num} is = {result}")

        elif choice == '3':
            # Area & Perimeter
            print("\n--- AREA & PERIMETER ---")
            shape = input("Choose a shape (square, rectangle, circle): ").lower()

            if shape == 'square':
                side = float(input("Length of side: "))
                area = side ** 2
                perimeter = 4 * side
                print(f"Area: {area} | Perimeter: {perimeter}")
            elif shape == 'rectangle':
                length = float(input("Length: "))
                width = float(input("Width: "))
                area = length * width
                perimeter = 2 * (length + width)
                print(f"Area: {area} | Perimeter: {perimeter}")
            elif shape == 'circle':
                radius = float(input("Radius: "))
                pi = 3.1416
                area = pi * (radius ** 2)
                circumference = 2 * pi * radius
                print(f"Area: {area} | Circumference: {circumference}")
            else:
                print("Shape chosen is not known!")

        elif choice == '4':
            # Temperature Converter
            print("\n--- TEMPERATURE CONVERTER ---")
            temp_type = input("What temperature do you have? (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
            temp_val = float(input("Temperature value: "))

            if temp_type == 'C':
                # Celsius to F & K
                f = (temp_val * 9/5) + 32
                k = temp_val + 273.15
                print(f"Fahrenheit: {f} | Kelvin: {k}")
            elif temp_type == 'F':
                # Fahrenheit to C & K
                c = (temp_val - 32) * 5/9
                k = c + 273.15
                print(f"Celsius: {c} | Kelvin: {k}")
            elif temp_type == 'K':
                # Kelvin to C & F
                c = temp_val - 273.15
                f = (c * 9/5) + 32
                print(f"Celsius: {c} | Fahrenheit: {f}")
            else:
                print("Incorrect temperature type!")

        elif choice == '5':
            print("Thank you for using this calculator!")
            break

        else:
            print("Invalid option! Please choose again from 1-5.")



if __name__ == "__main__":
    main()
