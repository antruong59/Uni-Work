class NumbersIterable:
    def __init__(self, numbers):
        self.numbers = numbers
       
    def __iter__(self):
        return NumbersIterator(self.numbers)


class NumbersIterator: 
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
        
    def __next__(self):
        if self.index == len(self.numbers):
            raise StopIteration()

        number = int(self.numbers[self.index])
        self.index += 1
        return number

    
    

niterable = NumbersIterable(["1", 2.0, "4",5,6.1,"7",8,9.2])

sum = 0
for i in niterable:
    print(i)
    sum += i
print("sum =", sum)
