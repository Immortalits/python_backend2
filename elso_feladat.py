import unicodedata

# data = 'Szabó béláaáá145úúő'
# normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
# print(normal.decode("utf-8"))

nevek = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = []


def emailKeszit(lista):
    email = "@company.hu"
    nevekosszefuzve = ""
    for i in range(len(lista)):
        nev = unicodedata.normalize('NFKD', lista[i]).encode('ASCII', 'ignore')
        if not i == len(lista) - 1:
            nevekosszefuzve = nevekosszefuzve + nev.decode("utf-8") + "."
        else:
            nevekosszefuzve = nevekosszefuzve + nev.decode("utf-8")
    vegleges = nevekosszefuzve + email
    return vegleges.lower()


for nev in nevek:
    dictionary = {}
    dictionary["name"] = nev
    dictionary["email"] = emailKeszit(nev)
    dictionary["password"] = nev[0] + "123Start"
    users.append(dictionary)


def kiir(users):
    users = sorted(users, key=lambda dictionary: dictionary["name"])
    with open("nevek.txt", "w", encoding="UTF-8") as fajl:
        for user in users:
            nev_kiir = ""
            for nev in user["name"]:
                nev_kiir += nev + " "

            fajl.write(f"{user['name']} {user['email']} {user['password']} \n")


kiir(users)