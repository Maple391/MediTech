with open("Usersystemlogin.csv") as csv:
    lines = csv.readlines()
    for i in range(1, len(lines)):
        parsedline = lines[i].split(",")
        users = [
            parsedline[0],
            parsedline[1],
        ]