from random import randrange


def test_random():
    # Random number between 0-99
    number = randrange(100)
    while True:
        guess = int(input("? "))
        if guess == number:
            print("You got it!")
            break


def exeption_hierarchy():
    s = [1, 4, 6]
    #print(s[28])
    # Key error
    d = dict(a=65, b=66, c=67)
    print(d['g'])


def lookups():
    s = [1, 2, 3]
    try:
        item = s[5]
    #except IndexError:
    except LookupError:
        print("Got an IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    #except KeyError:
    except LookupError:
        print("Got an KeyError")


def median(iterable):
    """
    Obtain the central value of a series.
    Sorts the iterable and returns the middle value:
        If there is an odd number of elements
    Or the arithmetic mean of the middle two elements
    if there is an even number of elements
    :param iterable: A series of orderable items
    :return: the median of the series.
    """
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() arg is an empty list")
    # integer division //
    median_index = (len(items) -1)//2
    # Odd number of member
    if len(items) % 2 != 0:
        return items[median_index]

    return (items[median_index] + items[median_index + 1])/2.0


def test_median():
    """
    Exception payloads are strings and are passed as a single
    argument to an exception constructor.
    Use args exception attribute.

    Output is a single element Tuple containing the message that
    was passed to the constructor.
    Another way is to use the str() constructor method.
    Reference: PEP 352
    """
    try:
        median([])
    except ValueError as e:
        print("Payload:", e.args)
        print(str(e))


def more_info():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print('encoding:', e.encoding)
        print('reason:', e.reason)
        print('object:', e.object)
        print('start:', e.start)
        print('end:', e.end)


def main():
    more_info()
    #test_median()
    # Odd number
    #print(median([5, 2, 1, 4, 3]))
    # Even number
    #print(median([5, 2, 1, 4, 3, 6]))
    # Empty list
    #print(median([]))
    #lookups()
    #test_random()
    #exeption_hierarchy()


if __name__ == '__main__':
    main()
    exit(0)