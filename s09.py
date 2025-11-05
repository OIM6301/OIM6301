# pi = 3.1415926
# print(f"Value of pi: {pi:.3f}")
# print(round(pi, 4))

r1 = 2
r2 = 10
r3 = 42
r4 = 100

# a1 = 3.14 * r1**2
# a2 = 3.14 * r2**2
# a3 = 3.14 * r3**2
# a4 = 3.14 * r4**2

# print(a1)
# print(a2)


def calc_area(radius):
    """
    Calculate the area of a circle given radius and return it
    """
    pi = 3.1415926
    area = pi * radius * radius
    # print(area) # Display it, kind of like a side effect
    # if the function does not explicitly return a value, it will return None
    return area


# calc_area(r1)  # 12.5663704
# calc_area(r2)  # 314.15926
# calc_area(20)  # calling a function

# calculate the total area of two circles (r1, r2)
a1 = calc_area(r1) 
# print(type(a1))
a2 = calc_area(r2)
print(a1 + a2)

def double(x):
    return 2 * x


# what is twice the area of circle with radius r3?
area_r3 = calc_area(r3)
twice_area_r3 = double(area_r3)
print(twice_area_r3)