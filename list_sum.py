def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.

    @param numbers (list of int): List of integer numbers.

    @return int: Sum of the list elements.
    """

    # TODO: set a running total variable
    total = 0

    # use a loop to calculate the sum of all numbers in the list
    for n in numbers:
        total += n

    # return the sum
    return total


if __name__ == "__main__":
    nums = [5, 19, 2, 33, -5, 2]
    # call function sum_list() and send argument 'nums', then print it out for testing
    print(sum_list(nums))
