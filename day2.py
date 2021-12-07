f = open("input2.txt","r")
input = f.readlines()
depth = 0
forward = 0
aim = 0
for index,val in enumerate(input):
  #  print(index,val)
  if val.find("\n") == -1:
      print("valfind == -1")
      number = int(val[val.find(' ')+1].strip())
      print(number)
  else:
    number = int(val[val.find("\n")-1].strip())
    print(number)

  if val.find("forward") != -1:
      forward = forward + number
      depth = depth + (aim*number)
  elif val.find("up") != -1:
      aim = aim - number
  elif val.find("down") != -1:
      aim = aim + number
print ("depth: ",depth,"forward: ",forward, "koordinates: ",depth*forward)