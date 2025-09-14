Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print("     ")

answer1 = int(input("(Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk  \n :"))

if answer1 == 1:
  Gryffindor += 1
elif answer1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong answer")

answer2 = int(input("Q2) When I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold  \n :"))

if answer2 == 1:
  Hufflepuff += 2
elif answer2 == 2:
  Slytherin += 2
elif answer2 == 3:
  Ravenclaw += 2
elif answer2 == 4:
  Gryffindor += 2 
else:
  print("Wrong answer")

answer3 = int(input("Q3) Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum  \n :"))

if answer3 == 1:
  Slytherin += 4
elif answer3 == 2:
  Hufflepuff += 4
elif answer3 == 3:
  Ravenclaw += 4
elif answer3 == 4: 
  Gryffindor += 4 
else:
  print("Wrong answer")

if  Slytherin > Hufflepuff and Slytherin > Ravenclaw and Slytherin > Gryffindor:
  finalRole = "Slytherin"
elif Hufflepuff > Ravenclaw and Hufflepuff > Gryffindor:
  finalRole = "Hufflepuff"
elif Ravenclaw > Gryffindor:
  finalRole = "Ravenclaw"
else:
  finalRole = "Gryffindor"


print("Your scoreboard: \n Slytherin: " + str(Slytherin) + " \n Hufflepuff: " + str(Hufflepuff) + " \n Ravenclaw: " + str(Ravenclaw) + " \n Gryffindor: " + str(Gryffindor))
print("So, CONGRATULATIONS, you are a " + finalRole)
