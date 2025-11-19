# Strategy?

# I want to create 2 functions
# 1. Run one simulation
# 2. repeat simulation 10 times
import random


def simulation(n=100):
    """One simulation of rolling n dice"""
    # print('One simulation: 100')  # Fake it till make it
    total = 0
    for i in range(n):
        random_number = random.randint(1, 6)
        total += random_number
    return total, total / n


def repeat_simulations(n=10):
    """Repeat simulations n times"""
    for i in range(n):
        total, avg = simulation(1000000)
        print(f"Simulation {i + 1}: Total = {total}, Average = {avg}")


# repeat_simulations()


def main():
    # s = simulation()
    # print(s)
    n = input("How many simulations to run? ")
    repeat_simulations(int(n))


if __name__ == "__main__":
    main()
