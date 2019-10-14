
class Val(object):
        __slots__=['value']
        def __init__(self, value = 0):
            self.value = value
        def __repr__(self):
            return f'Val({self.value})'
        def eval(self):
            return self.value

v = Val(1)
print(v)
assert v.eval() == 1

class Add(object):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left + self.right

v = Add(1, 2) #1+2
assert v.eval() == 3