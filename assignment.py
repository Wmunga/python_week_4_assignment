with open('assignment.txt', 'r') as file:
    content = file.read()
    print(content)

with open('assignment.txt', 'w') as file:
    file.write("I think I am finally understanding how this actually works.")
    content = file.write()
    print(content)



