# domosi123{}}123domosi123:=(*)<>1domosi1
bemenet = 'domosi123{}}123domosi123:=(**)<>1domosi1'


import re

azonosito = re.compile('[a-zA-Z]+[a-zA-Z0-9]*')
konstans = re.compile('[0-9]+')
kommentar1 = re.compile('{.*?\}')
kommentar2 = re.compile('\(\*.*?\*\)')
ertekadas1 = re.compile(':=')
ertekadas2 = re.compile('<[>=]')
ertekadas3 = re.compile('>=')

final = []

for char in bemenet:
    # print(bemenet)

    if str.isalpha(char):
        if azonosito.match(bemenet):
            match = azonosito.match(bemenet)
            final.append("<azonosító>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif str.isnumeric(char):
        if konstans.match(bemenet):
            match = konstans.match(bemenet)
            final.append("<konstans>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif char == '{':
        if kommentar1.match(bemenet):
            match = kommentar1.match(bemenet)
            final.append("<kommentár>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif char == '(':
        print(kommentar2.match(bemenet))
        if kommentar2.match(bemenet):
            match = kommentar2.match(bemenet)
            final.append("<kommentár>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif char == ':':
        if ertekadas1.match(bemenet):
            match = ertekadas1.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif char == '<':
        if ertekadas2.match(bemenet):
            match = ertekadas2.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    elif char == '>':
        if ertekadas3.match(bemenet):
            match = ertekadas3.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]
            print(bemenet)

    else:
        # print("unkwown char: " + char)
        final.append(char)
        bemenet = bemenet[1:]
        continue


print(final)
