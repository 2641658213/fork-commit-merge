# Python - Easy

# TODO: Create a Simple Python Program that:
# lists the first 10 natural numbers,
# prints that list to the console and,
# prints the sum of the numbers of that list

def function(numbers):
    # Create a list of the first 10 natural numbers
    numbers = list(range(1, 11))

    # Print the created list to the console
    print("List of the first 10 natural numbers:", numbers)

    # Print the sum of the numbers in the list
    sum_of_numbers = sum(numbers)
    print("Sum of the numbers in the list:", sum_of_numbers)

