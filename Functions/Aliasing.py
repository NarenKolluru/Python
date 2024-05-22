def greets():
    print("Welcome")
wish=greets
greets()
wish()
print(id(wish),id(greets))
