import random


def generator(n, starting, ending):
    """
    This function generates multiple random integer numbers, and return them as
    a list.

    @param n (int), number of numbers to generate
    @param starting (int), starting value of the random number range, inclusive
    @param ending (int), ending value of the random number range, inclusive

    @return (list), put all generated random integers into a list, and return it
    """

    numbers = []

    # use loop to generate n random integers between starting and ending (inclusive)
    for _ in range(n):
        num = random.randint(starting, ending)
        numbers.append(num)

    return numbers


if __name__ == "__main__":
    print(generator(5, 1, 10))
    print(generator(3, -5, 5))
