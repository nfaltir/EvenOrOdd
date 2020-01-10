def evenOdd():

    print("\n====================Even or Odd====================\n")

    anyNum = int(input("Please enter any real number: "))  # user input
    while anyNum != 0:

        if anyNum % 2 == 0:  # simple boolean structure with the modulos operator
            print("\n", anyNum, "= Even number\n")
        else:
            print("\n", anyNum, "= Odd number\n")
        anyNum = int(
            input("Please enter any real number or enter '0' to quit: "))


evenOdd()
