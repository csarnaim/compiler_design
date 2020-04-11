import re

# bemenet = 'domosi123{}123domosi123:=(**valami*)<>1domosi1'


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
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 2")
                elif (i == vag[1] - 1):
                    final.append("3")
                else:
                    final.append("2")
            bemenet = bemenet[vag[1]:]

    elif str.isnumeric(start):
        if konstans.match(bemenet):
            match = konstans.match(bemenet)
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 4")
                elif (i == vag[1] - 1):
                    final.append("5")
                else:
                    final.append("4")
            bemenet = bemenet[vag[1]:]

    elif start == '{':
        if kommentar1.match(bemenet):
            match = kommentar1.match(bemenet)
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 6")
                elif (i == vag[1] - 1):
                    final.append("7")
                else:
                    final.append("6")
            bemenet = bemenet[vag[1]:]

    elif start == '(':
        if kommentar2.match(bemenet):
            match = kommentar2.match(bemenet)
            vag = match.span()
            flag = 0
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 8")
                elif (i == 1):
                    final.append("9")
                elif (i > 1 and char == "*"):
                    final.append("10")
                    flag = 1
                elif (i == vag[1] - 1):
                    final.append("11")
                else:
                    if (flag == 0):
                        final.append("9")
                    else:
                        final.append("10")
            bemenet = bemenet[vag[1]:]

    elif start == ':':
        if ertekadas1.match(bemenet):
            match = ertekadas1.match(bemenet)
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 12")
                else:
                    final.append("13")
            bemenet = bemenet[vag[1]:]

    elif start == '<':
        if ertekadas2.match(bemenet):
            match = ertekadas2.match(bemenet)
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 14")
                else:
                    if (char == "="):
                        final.append("15")
                    else:
                        final.append("16")
            bemenet = bemenet[vag[1]:]

    elif start == '>':
        if ertekadas3.match(bemenet):
            match = ertekadas3.match(bemenet)
            vag = match.span()
            for i, char in enumerate(match.group()):
                if (i == 0):
                    final.append("1 17")
                else:
                    final.append("18")
            bemenet = bemenet[vag[1]:]

    else:
        raise InvalidTokenError(start, eredeti_hossz - len(bemenet) + 1)

print(*final, sep=' ')
