def sum_two_numbers(a, b):
    return a + b  # Return result to the function caller


c = sum_two_numbers(3, 12)  # Assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = b + a
        a = tmp_var
    return result


print(fib(10))
