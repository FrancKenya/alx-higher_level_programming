#!/usr/bin/python3

""" Prints a text with two lines """


def text_indentation(text):
    """ This function prints a text with two lines after each of these
    characters: ., ?, :
    Text: Is a string otherwise raise a TypeError
    """
    # check if text is a string and raise a type error if not
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # initialize a boolean to track where change will be made
    double_line_activation = False

    # check the text for either of the 3 characters
    for char in text:
        if char in ['.', '?', ':']:
            # set to true if found and print rest of the text to that point
            double_line_activation = True
            print(char, end='')
        else:
            # print all if not found
            print(char, end='')

        if double_line_activation:
            # if found add the two lines
            print('\n\n', end='')
            double_line_activation = False
