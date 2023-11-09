import random, os , time

def  roll_dice(sides):
  result = random.randint(1,sides)
  return result

def health():
  status =  ((roll_dice(6)*roll_dice(12))/2)+10
  return status
def Strength():
  str = ((roll_dice(6)*roll_dice(12))/2)+12
  return str

os.system("clear")
print("\033[33m")
print("            Character Builder")
time.sleep(1)
print
print("\033[37m")
name = input("enter your Legend:")
character_type = input("enter your character type:")
print()
print()
name1 = input("enter your Legend:")
character_type1 = input("enter your character type:")
print()
time.sleep(3)
print(name)
n1 = Strength()
a = health()
print("\033[32m")
print("HEALTH", health())
print("STRENGTH",Strength())
print()
print()
print("\033[0m")
print(name1)
print("\033[32m")
print("HEALTH", health())
b = health()
print("STRENGTH",Strength())
print("\033[0m")
print("their battle begins in few seconds ")
n2 = Strength()
print()
round = 1
winner = None
while True:
  time.sleep(5)
  os.system("clear")
  print("\033[38m")
  print("      ⚔️  BATTLE TIME ⚔️ ")
  print()
  print("\033[30m")
  print("  The Battle Begins")
  print("\033[0m")
  name_dice = roll_dice(6)
  nam1_dice = roll_dice(6)
  diff = abs(n1 - n2)+1
  if name_dice > nam1_dice:
    b -= diff
    a -= diff
    if round == 1:
      print("\033[38m")
      print(name,"wins the",round," round")
      print(name1,"takes the damage-",b/3)
    else:
      print(name1,"wins the",round,"th battle")
      print(name,"takes the damage-",a/3)
  else:
    print("they draw the round-",round)
  print("\033[0m")
  print()
  print(name)
  print("\033[32m")
  print("HEALTH:",a)
  print()
  print("\033[0m")
  print(name1)
  print("\033[32m")
  print("HEALTH:",b)
  print()

  if a<=0:
    print("\033[31m")
    print(name,"has died!")
    winner = name1
    break
  elif b<=0:
    print("\033[31m")
    print(name1,"has died!")
    print("\033[0m")
    winner = name
    break
  else:
    print("\033[0m")
    print("And they're both standing for the next round")
    round += 1
time.sleep(10)
os.system("clear")
print("\033[0m")
print("      ⚔️ BATTLE TIME ⚔️ ")
print()
print("\033[31m")
print(winner,"has won the Battle")
  