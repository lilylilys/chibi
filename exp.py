
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