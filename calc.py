def calc(s):
    print('s=', s)
    nums = map(int, s.split('+'))
    #print('nums=', nums)
    return sum(nums)

print(calc("1+2"))
