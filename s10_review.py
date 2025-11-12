def square(n):
    """Calculate the square of given n"""
    result = n * n
    return result


# x = 10
# result = square(x)


# number = input('Please enter a number: ')

# if int(number) > 90:
#     print('A')
# elif int(number) > 80:
#     print('B')
# else:
#     print('It is a small number.')

# a = 10
# print(isinstance(a, int))
# print(isinstance(a, float))


def calc(a, b):
    """"""
    s = a + b
    p = a * b
    return s, p


# result1, result2 = calc(10, 20)
# print(result1)
# print(result2)
# result = calc(10, 20)
# print(result)
# print(type(result))


def f():
    print("Hi")
    # return None


# result = f()
# print(result)

# score = 70
# if score >= 90:
#     print("A")
# elif score >= 60:
#     print("Pass")
# else:
#     print("Fail")


def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "Pass"  # return immediately stops the function
    else:
        return "Fail"


# result = check_grade(95)
# print(result)


def check_grade_bad(score):
    score = int(
        input("Enter your score: ")
    )  # This will override the function parameter
    if score >= 90:
        return "A"
    elif score >= 60:
        return "Pass"  # return immediately stops the function
    else:
        return "Fail"


# print(check_grade_bad(95))


def check_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
    else:
        if bmi >= 18.5 and bmi < 25:
            print("Normal Weight")
        else:
            if bmi >= 25 and bmi < 30:
                print("Overweight")
            else:
                print("Obesity")


check_bmi(22.5)
check_bmi(17.5)
check_bmi(27.5)