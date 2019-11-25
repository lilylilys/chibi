import pegpy

peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Value #Mul })*
Value = { [0-9]+ #Int }
''')
parser = pegpy.generate(peg)

t = parser('1+2*3')
print(repr(t))

def calc(t):
    if t == 'Int':
        return int(str(t))
    if t == 'Add':
        return calc(t[0]) + calc(t[1])
    if t == 'Mul':
        return calc(t[0]) * calc(t[1])
    print(f'TODO {t.tag}')
    return 0

t = parser('1+2*3+4*5')
print(repr(t))
print(calc(t))

