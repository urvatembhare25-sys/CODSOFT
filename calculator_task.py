 
print("\n----- CALCULATOR -----")

num1, num2=input("enter two numbers:").split()
num1 = int(num1)
num2 = int(num2)

while True:
    print("\n1. Addition")
    print("2. Subraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent (power)")
    print("6. Remainder (modulus)")
    print("7. Floor Division")
    print("8. Exiting calculator...")

    select=int(input("select operation:"))

    match select:
        case 1:
            print(f"Addition of {num1}+{num2}:", num1+num2)

        case 2:
            print(f"Subtraction of {num1}-{num2}:", num1-num2)

        case 3:
            print(f"Multiplication of {num1}*{num2}:", num1*num2)

        case 4:
            if (num2 == 0):
                print("Error! Cannot divide by zero.")
            else:
                print(f"Division of {num1}/{num2}:", num1/num2)

        case 5:
            print(f"Exponential of {num1}**{num2}:", num1**num2)

        case 6:
            print(f"Remainder of {num1}%{num2}:", num1%num2)

        case 7:
            print(f"Floor Division of {num1}//{num2}:", num1//num2)

        case 8:
            print("Exiting calculator...")
            break

        case _:
            print("Invalid Operation! Try again.")