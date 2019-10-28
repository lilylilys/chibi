from exp import Val, Add, Sub, Mul, Div

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1), parse(s2))
    if s.find('*') > 0:
        pos = s.find('*')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Mul(parse(s1), parse(s2))
    if s.find('-') > 0:
        pos = s.find('-')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Sub(parse(s1), parse(s2))
    if s.find('/') > 0:
        pos = s.find('/')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Div(parse(s1), parse(s2))
    return Val(int(s))

e = parse("1-2-3")
print(e, e.eval()) # -4
