num1 = int(input("Enter a number: "))

if num1 > 0 and num1 % 2 == 0 :
    print("The number is positive and even.")
elif num1 > 0 and num1 % 2 != 0 :
    print("The number is positive but not even.")

elif num1 < 0 and num1 % 2 == 0 :
    print("The number is not positive but even.")
else:
    print("The number is neither positive nor even.")
