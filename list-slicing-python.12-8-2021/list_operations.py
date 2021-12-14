"""Utilities for manipulating lists."""


def head(input_list):
    # """Return the first item of the input list.

    # For example:

    head(['Jan', 'Feb', 'Mar'])

    #   'Jan'
    # # """
    return head([0])


def tail(input_list):
    # """Return a new list of all items, excluding the first item.

    # For example:

    tail(['Jan', 'Feb', 'Mar'])

    # ['Feb', 'Mar']

    # """

    return tail[1:]


def last(input_list):
    # """Return the last item of the input list.

    # For example:

    # >>>
    last(['Jan', 'Feb', 'Mar'])
    # 'Mar'

    # """

    return last([2])


def top(input_list):
    # """Return all elements of the input list except the last.

    # For example:

    top(['Jan', 'Feb', 'Mar'])
    # ['Jan', 'Feb']

    # """

    return top[:2]


def first_three(input_list):
    # """Return the first three elements of the input list.

    # For example:

    first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    # ['Jan', 'Feb', 'Mar']

    # """

    return first_three[0:2]


def last_five(input_list):
    # """Return the last five elements of the input list.

    # For example:

    last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    # [15, 18, 21, 24, 27]

    # """

    return last_five[6:]


def middle(input_list):
    # """Return all elements of input_list except the first two and the last two.

    # For example:

    middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    # [6, 9, 12, 15, 18, 21]

    # """

    return middle[2:7]


def inner_four(input_list):
    # """Return the third, fourth, fifth, and sixth elements of input_list.

    # For example:

    inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    # [6, 9, 12, 15]

    # """

    return inner_four[2:5]


def inner_four_end(input_list):
    # """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    # This function should return those elements in a list, in the exact order
    # described above.

    # For example:

    inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    # [12, 15, 18, 21]

    # """
    return inner_four_end[7:4]


def replace_head(input_list):
    # """Replace the head of input_list with the value 42 and return nothing.

    # For example:

    multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    input_list[0] = 42
    # >>> replace_head(multiples)
    # >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    # True

    # """
    replace_head(multiples)
    pass


def replace_third_and_last(input_list):
    # """Replace third and last elements of input_list with 37 and return nothing.

    # For example:

    multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    input_list[2] = 37
    input_list[9] = 37

    # >>> replace_third_and_last(multiples)
    # >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    # True

    # """
    replace_third_and_last(multiples)
    pass


def replace_middle(input_list):

  input_list[2:-2] = [42, 37]
    # >>> replace_middle(multiples)
    # >>> multiples == [0, 3, 42, 37, 24, 27]
    # True
  pass
multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
replace_middle(multiples)
    # """

def delete_third_and_seventh(input_list):
  del input_list[2]
  del input_list[5]

notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
delete_third_and_seventh(notes)

    # """
pass


def delete_middle(input_list):
    # """Remove all elements from input_list except the first two and last two.

    # Return nothing.

    # For example:
    del input_list[2:-2]

    notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    delete_middle(notes)
    notes == ['Do', 'Re', 'Ti', 'Do']
    True

    # """

    pass


# This is the part were we actually run the doctests.

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')
