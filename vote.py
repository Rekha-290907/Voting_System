age = int(input("Enter your age: "))
print("Welcome to voting system")

if age >= 18:
    print("You are eligible for voting")
    print("You can register as voter")
else if age < 18:
    print("You are not eligible for voting")
    print("You must be atlest 18 years old")
