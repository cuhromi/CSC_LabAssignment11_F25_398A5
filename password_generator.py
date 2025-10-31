import random


def generate_password(length, use_digits, use_special):
    """
    Generate a random password with customizable options.

    @param length (int): The length of the password. Default is 12.
    @param use_digits (bool): Whether to include digits (0-9)
    @param use_special (bool): Whether to include special characters

    @return (str): Randomly generated password.
    """

    # possible character strings
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "!@#$%^&*()_+"

    possible_characters = ""
    # always include letters
    possible_characters = lower_letters + upper_letters

    # include digits if requested
    if use_digits:
        possible_characters += digits

    # include special characters if requested
    if use_special:
        possible_characters += specials

    # build a list from possible_characters so each character is an item
    char_list = list(possible_characters)

    password = ""
    # use loop to generate the random password
    for _ in range(length):
        password += random.choice(char_list)

    return password


if __name__ == "__main__":
    print(generate_password(12, True, True))
    print(generate_password(14, True, False))
    print(generate_password(16, False, True))
    print(generate_password(18, False, False))
