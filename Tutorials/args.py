def add(*args):
    sum = 0
    args= list(args)
    args[0]=7
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4))

