
import second

def SayHello():
  # En enkel funktion som endast skriver ut text
  print("Var h�lsad, fr�mling!")
def Hejsan(name):
  # En funktion som tar emot en parameter och skriver ut den med en text
  print("Hall� d�r, " + name)
def Addition(tal1, tal2):
  #Denna metod tar emot tv� parametrar och skickar tillbaka ett returv�rde
  x = tal1 + tal2
  return x 
def SameName(x):
  x = x + 2
  print(x)
  return x



print("Nu startar programmet!")
SayHello() 
Hejsan("Delia")
print("Summan av talen 1 och 2 �r: {0}".format(Addition(1,2)))

x = 5
print("Mitt startv�rde �r {0} och mitt ber�knade v�rde �r {1}, men b�da anv�nder sama variabelnamn!".format(x, SameName(x)))

second.second()