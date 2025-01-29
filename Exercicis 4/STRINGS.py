year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif 1900 < year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
