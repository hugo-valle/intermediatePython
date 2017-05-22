import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("Running '{0}' with arguments {1}".format(
            func.__name__, args))

        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


def test_raise_to():
    square = raise_to(2)
    print(square(5))
    print(square(9))
    cube = raise_to(3)
    print(cube(5))
    print(cube(9))


def main():
    # Function Factory
    add_logger = logger(add)
    sub_logger = logger(sub)

    print(add_logger(3, 3))
    print(add_logger(4, 9))

    print(sub_logger(3, 3))
    print(sub_logger(4, 9))


if __name__ == '__main__':
    #main()
    test_raise_to()
    exit(0)