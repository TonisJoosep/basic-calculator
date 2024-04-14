from calculator_functions import plus_operation, minus_operation, multiplication_operator
from calculator_functions import division_operator
print("")
print("Hello! This is a simple calculator.")
print("")
history_pick = input("Press 'h' for calculation history or any other key to use calculator\n")
while history_pick == "h":
    with open("result.txt", "r") as calculation:
        calculation_storage = calculation.readlines()
        print(calculation_storage)
        history_pick = input("'h' to have another look or continue?\n")
else:
    pass

continue_calculation = "y"
while continue_calculation == "y":

    number_1 = input("Enter first number: ")
    while number_1.replace(".", "", 1).isdigit():
        break
    else:
        print("Only numerals are valid (1,2,3...etc)")
        continue
    while True:
        operator = input("+, -, / or *:")
        if operator in ["+", "-", "/", "*"]:
            break

    number_2 = input("Enter second number: ")
    while number_2.replace(".", "", 1).isdigit():
        break
    else:
        print("Only numerals are valid 1,2,3...etc")
        continue
    while operator == "/" and number_2 == "0":
        try:
            number_2 = float(input("Can't divide by 0, try a different number: "))
        except number_2 == 0:
            continue
        else:
            break

    if operator == "+":
        operation_result = plus_operation(number_1, number_2)
    elif operator == "-":
        operation_result = minus_operation(number_1, number_2)
    elif operator == "*":
        operation_result = multiplication_operator(number_1, number_2)
    elif operator == "/":
        operation_result = division_operator(number_1, number_2)
    else:
        exit("Wrong operation, run code again")

    if operation_result.is_integer():
        operation_result = int(operation_result)
    else:
        operation_result = round(operation_result, 2)
    result = f"{number_1} {operator} {number_2} = {operation_result}"

    print(result)

    with open("result.txt", "a") as calculation:
        calculation_storage = calculation.write(f"{str(result)}\n")

    print("Do you want to calculate something else?")
    continue_calculation = input("y/n: ")
print("So quit, and see if we care!")
