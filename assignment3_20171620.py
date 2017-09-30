import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                if len(parse) == 4:
                    if parse[1].isalpha() == True and int(parse[2]) and int(parse[3]):
                        record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                        scdb += [record]
                    else:
                        print("TypeError")
                else:
                    print("LengthError")
            except:
                print("TypeError")
                continue

        elif parse[0] == 'del':
            check_scdb = scdb[:]
            for l in range(len(scdb)):
                k = scdb[len(scdb)-l-1]
                if k['Name'] == parse[1]:
                    scdb.remove(k)
            for j in range(len(scdb)):
                p = scdb[len(scdb)-j-1]
                if p['Name'] == parse[1]:
                    scdb.remove(p)
            if len(check_scdb) == len(scdb):
                print("Not Found")
                continue
            if len(parse) != 2:
                print("LengthError")

        elif parse[0] == 'find':
            rep = 0
            for k in scdb:
                if k['Name'] == parse[1]:
                    rep += 1
                    print("Age=%s Name=%s Score=%s" % (k['Age'], k['Name'], k['Score']))
            if rep == 0:
                print("Not Found")
            if len(parse) != 2:
                print("LengthError")

        elif parse[0] == 'show':
            if len(parse) == 1:
                sortKey = 'Name'
            elif len(parse) == 2:
                if parse[1] == 'Name':
                    sortKey = 'Name'
                elif parse[1] == 'Age':
                    sortKey = 'Age'
                elif parse[1] == 'Score':
                    sortKey = 'Score'
                else:
                    print("TypeError")
                    continue
            else:
                print("TypeError")
                continue
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'inc':
            try:
                rep = 0
                for j in scdb:
                    if j['Name'] == parse[1]:
                        rep += 1
                        j['Score'] = str(int(j['Score']) + int(parse[2]))
                if rep == 0:
                    print("Not Found")
            except ValueError:
                print("ValueError")
                continue
            if len(parse) != 3:
                print("LengthError")
                continue

        elif parse[0] == 'quit':
            if len(parse) != 1:
                print("LengthError")
                continue
            else:
                break

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


