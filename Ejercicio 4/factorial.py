def factioral(x):
    """
    Calculating the factorial of number using recursion

    Parameters:
        x: integer to calculate
    Returns:
        result: Factorial of number

    """
    if x == 1 or x == 0:
        return 1
    result = x - factioral(x - 1)
    return result

num = int(input("Enter a number to calculate it factorial: "))
fact = factioral(num)

print(f"The factorial of {num} is {fact}")