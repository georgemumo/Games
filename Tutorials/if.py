import time
name = ""
while len(name)==0:
    name = input("Enter your name: ")
print("Hello " + name)

num = 1
while num <= 5:
    print(num*"*")
    num += 1

for i in range(5,120,2):
    print(i+1)
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(0)
rows = int(input("Enter number of rows: "))
columnss = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")
for i in range(rows):
    for j in range(columnss):
        print(symbol,end=" ")
    print()
