import icontract

@icontract.require(lambda x: x > 3)
def f(x,y):
    print(x+y)

f(5,4)
