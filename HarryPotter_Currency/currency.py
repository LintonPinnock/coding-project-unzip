
def currency():
   # declare variables
    Sickle = 29
    Galleon = 493
    knuts = 0
    Sickles = 0
    Galleons = 0

    knut = int(input("Enter the currency in knuts   "))
    if knut >= Sickle:  # comparing the input to galleon because 1 galleon = 493 knuts
        Galleons = knut / Galleon  # if the knut is greater than 1 galleon divide the knuts by galleon and store the value in galleons
        knuts = knut % Galleon  # And store the remainder as Knuts
        if knuts > Sickle:  # if the remainder is greater than Slick, which is 29
            Sickles = knuts/Sickle  # divide the knuts (remainder) by Sickle.
            knuts = knuts % Sickle # used the remainder as the new value of knuts
    elif knut >= Sickle:  # Comparing the input to Sickle if its equal are greater than.
        Sickles = knut / Sickle  # save the quotient as sickles
        knuts = knut % Sickle # save the remainder as knuts

    elif knut < Sickle: # comparing input to sickle. if knut is less than Sickle
        knuts = knut   # save the number that is enter as knuts
    print("Galleons: ",int(Galleons),"Sickles: ",int(Sickles),"Knuts: ",int(knuts))
while True: # Run the function over and over until it is terminated.
    currency()



















