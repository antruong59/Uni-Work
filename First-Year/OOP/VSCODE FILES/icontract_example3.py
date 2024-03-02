import icontract

@icontract.require(lambda x,y: isinstance(x, int) and isinstance(y, int) and (x > 4) and (y>3))
@icontract.ensure(lambda result: result > 10)
def f(x,y):
    print(x+y)
    return x+y

f(5,4)
