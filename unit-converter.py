print("Hello! I'm Unit Converter and I can convert kilometers into mails and the other way around.")

choose_conversion = str(input("For converting km --> mi type in: 'km' and for converting mi --> km type in 'mi': "))

while True:
    if choose_conversion == "km":
        km = input("Kilometers to convert (number only): ")
        km = float(km.replace(",", "."))    # replacing comma with dot
        miles = km * 0.621371
        print("{0} km is {1} mi.".format(km, miles))
    elif choose_conversion == "mi":
        mi = input("Miles to convert (number only): ")
        mi = float(mi.replace(",", "."))    # replacing comma with dot
        kilometers = mi / 0.621371
        print("{0} mi is {1} km.".format(mi, kilometers))

    choice = input("Would you like to do another conversion? (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print("Have a nice day and see you soon! ;)")
        break
