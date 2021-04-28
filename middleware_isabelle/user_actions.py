# The user actions is to feed, sleep and pet the lemur

# user action: try feed

# Startläge: Det är möjligt att mata
feed_possible = True
# Efter man har klickat på knappen för att mata
feed_possible = False
# Efter x antal minuter/timmar
feed_possible = True

# Meddelanden till användaren

if feed_possible = True:
    print("Feed the lemur")

else:
    print ("The lemur is fed")

# user action: try pet

# Startläge: Det är möjligt att klappa
pet_possible = True
# Efter man har klickat på knappen för att klappa
pet_possible = False
# Efter x antal minuter/timmar
pet_possible = True

# Meddelanden till användaren

if pet_possible = True:
    print("Pet the lemur")

else:
    print ("The lemur is petted")

# user action: try sleep

# Startläge: Det är möjligt att sova
sleep_possible = True
# Efter man har klickat på knappen för att sova
sleep_possible = False
# Efter x antal minuter/timmar
sleep_possible = True

# Meddelanden till användaren

if sleep_possible = True:
    print("Put the lemur to sleep")

else:
    print ("The lemur is sleeping")

# user action: create joke

# Startläge: Det är inte möjligt att skriva in skämt
joke_possible = False
# Efter att man har matat eller klappat
joke_possible = True
# Efter att man har skrivit in ett skämt
joke_possible = False

# Meddelanden till användaren

if joke_possible = True:
    print("Enter a joke")
    user_buildup = input("Enter a buildup: ")
    user_punchline = input("Enter a punchline: ")
    buildUpsD.append(user_buildup)
    punchLinesD.append(user_punchline)

else:
    print ("You can't enter a joke")