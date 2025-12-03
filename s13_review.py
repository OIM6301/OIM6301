# x = 10.23524643
# y = 20.643634
# z = 30.634
# print("x = {}, y = {}, z = {}".format(x, y, z))

# print(f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

# print(f"{x = }, {y = }, {z = }")

print('Finished something')

# try:
#     number = int(input('Please enter a number: '))
#     result = 2025 / number
#     print(result)
# except (ZeroDivisionError, ValueError):
#     print('❗ You just entered invalid number!')
# # except ValueError:
# #     print('You have to enter an integer!')
# finally:
#     print('No matter what happens, we will see it')

data = ['Bruce', 'Mariana', 'Mamdou', 2025, 'Santiago']

for name in data:
    try:
        print(name[0])
    except Exception:
        print('    This is not a string.')



print('Moving on to here!')

