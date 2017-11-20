credentials = input("Please enter your password")
password = "changeme"
trys = 1

while credentials != password:
    print("Invalid password")
    credentials = input("Please re-enter your password")
    trys += 1
    if trys > 4:
        print("Maximum attempts taken: ", trys, "!")
        print("Access denied!")
        print("Please press enter to exit and")
        print("contact security to reset your password!")
        break
    if credentials == password:
        print("Password accepted")
        print("You have taken", trys, "attempts" "!")
        break
