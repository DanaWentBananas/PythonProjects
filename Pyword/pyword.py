import functions as use

while True:
    print("Welcome to PyWord\n")
    print("---- Main Menu ----")
    print("1. New Game")
    print("2. See Hall of Fame")
    print("3. Quit\n")
    print("What would you like to do?")
    ans = input()

    if ans=="1":
        use.play()
    elif ans =="2":
        use.show()
    elif ans=="3":
        print("Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")

