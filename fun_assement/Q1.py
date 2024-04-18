def find_max(num1, num2, num3):
    max_of_first_two = max(num1, num2)
    max_of_three = max(max_of_first_two, num3)
    return max_of_three
num1 = 10
num2 = 20
num3 = 15
print("Maximum of the three numbers is:", find_max(num1, num2, num3))