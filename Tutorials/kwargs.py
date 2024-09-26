def foo(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


foo(tittle = "Prof",first='Bob', middle ="mumo",last='Smith')