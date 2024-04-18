users = []
Reformedusers = []


with open("Usersystemlogin.csv") as csv:
    lines = csv.readlines()
    for i in range(1, len(lines)):
        parsedline = lines[i].split(",")

        users.append([
            parsedline[0].strip("\n"),
            parsedline[1].strip("\n")
        ])
    csv.close()

def login():

    Userlogin = input("please input username:")
    Userpassword = input("please enter password:")
    passed = False

    for i in range(len(users)):
        if users[i][0] == Userlogin and users[i][1] == Userpassword:
            passed = True
            break
    if passed:
        print("Welcome")
    else:
        print("Access denied")

def signup():

    newlogin = input("please input username:")
    newpassword = input("please input password:")
    users.append([
        newlogin,
        newpassword

    ])
    with open("Usersystemlogin.csv","w",encoding='utf-8') as reformed:
        for user in users:
            parsedline = ",".join(user)
            Reformedusers.append(parsedline)
        reformedusers = "\n".join(Reformedusers)
        reformed.write(reformedusers)
signup()
#login()
print(users)