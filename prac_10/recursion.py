"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# TO DO: 1. write down what you think the output of this will be,
# TO DO: 2. use the debugger to step through and see what's actually happening

# print(do_it(5))
# I think the output for this will be 3.
# When I ran the debugger it walked throught the function showing the different function calls and how n got lower
# until it hit zero and started to calculate the answer.

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
    do_something(n - 1)

# TO DO: 3. write down what you think the output of do_something(4) will be,
# TO DO: 4. use the debugger to step through and see what's actually happening

# do_something(4)
# I think the output will be 16 9 4 1
# When the debugger ran it didn't print the square of every number from the input to 0 it printed the square any number
# smaller than 0.

# TO DO: 5. fix do_something() so that it works according to the docstring

# Recursion from scratch
def get_blocks_loop(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(get_blocks_loop(6))


def get_blocks(n):
    if n <= 0:
        return 0
    return n + get_blocks(n-1)


print(get_blocks(6))
