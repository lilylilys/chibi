
class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
#print(v)
assert v.eval() == 1

def toExpr(a):
    if not isinstance(a, Expr):
            a = Val(a)
    return a

class Binary(Expr):
    __slots__=['left', 'right']
    def __init__(self, a, b):
            self.left = toExpr(a)   #aとbは式
            self.right = toExpr(b)
    def __repr__(self):
        cname = self.__class__.__name__
        return f'{cname}({self.left},{self.right})'

class Add(Binary):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = toExpr(a)   # aとb は式
        self.right = toExpr(b)
    def eval(self):
        return self.left.eval() + self.right.eval()

e = Add(1,Add(1,2))
#print(e)
assert e.eval() == 4

e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6

class Sub(Binary):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = toExpr(a)   # aとb は式
        self.right = toExpr(b)
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(Binary):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = toExpr(a)   # aとb は式
        self.right = toExpr(b)
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Binary):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = toExpr(a)   # aとb は式
        self.right = toExpr(b)
    def eval(self):
        return self.left.eval() // self.right.eval()
