
counter = 0
fileobject = open("input.txt","r")
prev = 0
for index, val in enumerate(fileobject):
    current = int(val)
    if current > prev:
        counter = counter+1
    prev = current

print("first solution:",counter)
fileobject = open("input.txt","r")

counter = 0
numbers = fileobject.readlines()
x = range(1999)
for i in x:
    if i+3 > 1999:
        break
    current = int(numbers[i])+int(numbers[i+1])+int(numbers[i+2])
    nextt = int(numbers[i+1])+int(numbers[i+2])+int(numbers[i+3])
    if current < nextt:
        counter = counter+1


print("second solution:",counter)


