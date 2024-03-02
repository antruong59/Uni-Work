def fahrenheit(c):
    if (isinstance(c, int) or isinstance(c, float)) and not isinstance(c,bool):
        return c*(9/5)+32
    else:
        raise TypeError("Only int or float allowed.")
