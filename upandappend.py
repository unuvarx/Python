lst = []
name = input("Enter a name: ")
x = name[0].upper()
y = x+name
removed = y.replace(y[1], "")
lst.append(removed)
