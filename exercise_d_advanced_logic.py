# For the following list of numbers:

from nbformat import current_nbformat


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
sorted_numbers = numbers.sort()
difference = numbers[-1] - numbers[0]
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
holding_number = 0
for number in numbers:
    if number == 2 and holding_number == 2:
        print(True)
    elif number == 2:
        holding_number = number


# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.
