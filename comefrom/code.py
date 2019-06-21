from goto import comefrom, label

# fmt: off

a = 1
b = 5

label .teleport

a = 10

comefrom .teleport

print(a)
