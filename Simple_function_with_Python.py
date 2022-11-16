
import second

def SayHello():
  # En enkel funktion som endast skriver ut text
  print("Var hälsad, främling!")
def Hejsan(name):
  # En funktion som tar emot en parameter och skriver ut den med en text
  print("Hallå där, " + name)
def Addition(tal1, tal2):
  #Denna metod tar emot två parametrar och skickar tillbaka ett returvärde
  x = tal1 + tal2
  return x 
def SameName(x):
  x = x + 2
  print(x)
  return x



print("Nu startar programmet!")
SayHello() 
Hejsan("Delia")
print("Summan av talen 1 och 2 är: {0}".format(Addition(1,2)))

x = 5
print("Mitt startvärde är {0} och mitt beräknade värde är {1}, men båda använder sama variabelnamn!".format(x, SameName(x)))

second.second()