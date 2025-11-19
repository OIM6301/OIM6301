# break

# print("Example of break:")
# for i in range(1, 10):
#     if i % 3 == 0:
#         break
#     print(i)

# print("Exmaple of continue:")
# for i in range(1, 50):
#     if i % 7 == 0 or i % 10 == 7:
#         continue
#     print(i)


# n = 5
# while n > 0:
#     n = n - 2
#     print(n)


# for
# 1. when you know exactly how many times you want to iterate

for i in range(5):
    print("Iteration", i)

# 2. when you want to iterate over a specific range of integers

for i in range(1, 11, 2):  # 1 to 10
    print(i)


# 3. when you want to iterate over a collection (like a list, tuple, or string)

for c in "Bruce":  # iterate over each character in the string
    print(c.upper())


fruits = ["apple", "banana", "cherry"]  # This is a list of strings

for fruit in fruits:
    print(fruit.capitalize())


for number in [10, 20, 30, 40]:  # This is a list of integers:
    print(number**2)

d = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}

for key in d:  # iterate over the keys of the dictionary
    print(f"{key}: {d[key]}")


portfolio = [
    {"symbol": "AAPL", "price": 150, "shares": 10},
    {"symbol": "META", "price": 280, "shares": 50},
    {"symbol": "MSFT", "price": 300, "shares": 20},
]
# how to calculate the total value
total_value = 0
for stock in portfolio:
    total_value += stock["price"] * stock["shares"]

# Select price, shares from portfolio

print(total_value)


# while
# 1. when you want to create an infinite loop


def game():
    """"""


# while True:
#     game()


# 2. the number of iterations is unknown and should continue until a specific condition becomes False

# guess number game

def guess_number():
    """"""
    while True:
        guess = input("Guess a number between 1 and 10 (or type 'exit' to quit): ")
        if guess.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            break
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Try again.")
            continue
        import random

        number = random.randint(1, 10)
        if guess == number:
            print("Congratulations! You guessed the correct number!")
        else:
            print(f"Sorry, the correct number was {number}. Try again!")

# guess_number()

# 3. waiting for a specific event or condition to occur

# user and password authentication simulation

correct_username = "admin"
correct_password = "password123"

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login successful! Welcome!")
        break
    else:
        print("Invalid credentials. Please try again.")
