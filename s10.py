# for i in range(4):
#     print("🧱🧱🧱🧱🧱🧱")


# i = 0
# while i < 4:
#     print("🧱🧱🧱🧱🧱🧱")
#     i += 1


# draw a triangle instead of a square
# for i in range(4):
#     print("🧱" * (i + 1))


# for i in range(1, 5):
#     print(i)
#     print("🧱" * i)


# Sum up integers from 0 to 1000


def sum_up(n):
    """Sum up integers from 0 to n"""
    total = 0
    for i in range(n + 1):
        # print(f"In iteration {i}:")
        # print(f"  Before adding {i}, total is {total}")
        total = total + i
        # print(f"  After adding {i}, total becomes {total}")
        # print()
    return total


# result = sum_up(100)
# print(result)
# print(sum_up(10000))


def sum_evens(n):
    """Sum up even numbers from 0 to n (inclusive)

    eg. if n = 10, the function should return 0+2+4+6+8+10
    """
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            # total + i  # expression, not a statement
            total += i
    return total


def sum_evens_2(n):
    total = 0
    for i in range(0, n+1, 2):
        total += i
    return total

# result = sum_evens_2(10)
# print(result)  # 30



def sum_up_while(n):
    """Sum up integers from 0 to n, using while loop"""
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1
    return total


print(sum_up_while(100))  # 5050