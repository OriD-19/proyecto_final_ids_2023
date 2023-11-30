from colorama import Back, Style

def test_function(func, expected_output, *args):

    """
    Takes a function to test, a expected output for the test case,
    and the arguments to call the function that is being tested.

    Returns 0 if the test case is correct, 1 otherwise (False/True)
    """

    print("---------------------")
    print("Testing:", func.__name__)
    print("---------------------")
    print("Input:", *args)
    out = func(*args)
    print("Output:", out)
    print("Expected Output:", expected_output)
    print("********************")

    if out == expected_output:
        print(Back.GREEN, "ACCEPTED", Style.RESET_ALL)
        return 0
   
    print(Back.RED, "FAILED", Style.RESET_ALL)
    return 1
