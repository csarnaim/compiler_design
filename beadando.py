import re


# bemenet = 'domosi123{}123domosi123:=(**)<>1domosi1'


class InvalidTokenError(Exception):
    def __init__(self, expression, position):
        self.expression = expression
        self.position = position

    def __str__(self):
        return f'Értelmezhetetlen karakter {self.expression} a következő helyen {self.position}'


bemenet = input("Kérem az elemzendő szöveget: ")

eredeti_hossz = len(bemenet)

azonosito = re.compile('[a-zA-Z]+[a-zA-Z0-9]*')
konstans = re.compile('[0-9]+')
kommentar1 = re.compile('{.*?\}')
kommentar2 = re.compile('\(\*.*?\*\)')
ertekadas1 = re.compile(':=')
ertekadas2 = re.compile('<[>=]')
ertekadas3 = re.compile('>=')

final = []

while (len(bemenet) != 0):
    start = bemenet[0]

    if str.isalpha(start):
        if azonosito.match(bemenet):
            match = azonosito.match(bemenet)
            final.append("<azonosító>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif str.isnumeric(start):
        if konstans.match(bemenet):
            match = konstans.match(bemenet)
            final.append("<konstans>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif start == '{':
        if kommentar1.match(bemenet):
            match = kommentar1.match(bemenet)
            final.append("<kommentár>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif start == '(':
        if kommentar2.match(bemenet):
            match = kommentar2.match(bemenet)
            final.append("<kommentár>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif start == ':':
        if ertekadas1.match(bemenet):
            match = ertekadas1.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif start == '<':
        if ertekadas2.match(bemenet):
            match = ertekadas2.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    elif start == '>':
        if ertekadas3.match(bemenet):
            match = ertekadas3.match(bemenet)
            final.append("<értékadás>")
            vag = match.span()
            bemenet = bemenet[vag[1]:]

    else:
        raise InvalidTokenError(start, eredeti_hossz - len(bemenet) + 1)

print(*final, sep=' ')
