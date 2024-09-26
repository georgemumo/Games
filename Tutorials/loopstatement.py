while True:
    name = input("Enter your name: ")
    if name != "":

        break
    print("Hello"+name)

phonenumber = "123-456-7890"
for number in phonenumber:
    if number== "-":
        continue
    print(number,end="")

for i in range(1,11):
    if i == 5:
        pass
    else:
        print(i)