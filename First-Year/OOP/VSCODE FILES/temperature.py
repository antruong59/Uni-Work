class Temperature:
    def __init__(self, degree):
        self.__degree = degree
        if not type(self.__degree) is int:
            raise TypeError
    
    def get_celsius(self):
        return self.__degree

    def get_fahrenheit(self):
        return (9 * self.__degree / 5) + 32
