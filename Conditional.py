# Declaring variable
calificacion = input("Introduce tu calificacion del AZ900: ")

calificacion = int(calificacion)

# We ask if the score is lees than 700
if calificacion < 700 :
    print("See? If you just had studied!") # If it is under 700 it shows this
elif calificacion > 1000 :
    print ("Liar, liar! You cannot get that score!")
else : # if the previous if is not true, go to this line
    print ("congrats, you can get your certificate!") # Executes if no if is true

# Legality verifier
edad = input ("Type your age ")
edad = int(edad)

if edad >= 18 and edad <= 115 :
    print("Welcome to the bar!")
elif edad > 115 :
    print("If you come with your granny you get free service")
elif edad < 0 :
    print("Yeah sure, u a time traveler")
else :
    print("No cigs for u")