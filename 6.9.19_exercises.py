import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILIED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(f2c(212) == 100)
    test(f2c(32) == 0)
    test(f2c(-40) == -40)
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39 == 4))
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


def f2c(t):
    """ Returns integer value to nearest degree celius given value in fahrenheit.
    """
    c = (t - 32) * (5 / 9)
    c = round(c)
    return c


def c2f(t):
    """ Returns integer value to nearest degree in fahrenheit given value in celcius.
    """
    f = t / (5 / 9) + 32
    f = round(f)
    return f

test_suite()    # Here is the call to run the tests.