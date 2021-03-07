"""VARS"""
listOfCommands = ["load", "tell", "infer_all", ]    # TO CHECK VALID COMMAND
data = []   # HOLDS ALL DATA (HEAD, [BODY]) FROM TXT FILE
lines = []  # HOLDS LINES FROM TXT FILE
KB = []  # HOLDS VALID ITEMS FROM TELL
inferred = []  # NEEDED FOR EFFECTIVE INFERENCE OF ALL DATA


"""______________________________________________LOAD________________________________________________"""


##
# Load function to execute load command
def load(command):
    fileName = ""
    global lines
    for i in range(len("load "), len(command)):
        fileName += command[i]

    while True:
        try:
            f = open(fileName, "r")
            lines = f.readlines()
        except FileNotFoundError:
            print("Error! wrong file name or file path")
            return
        else:
            break

    # remove "\n" from list of lines
    while '\n' in lines:
        lines.remove('\n')

    # remove "\n" from end of each line
    for i in range(len(lines)):
        line = lines[i]
        correctLine = ""
        for j in range(len(line)):
            if line[j] != '\n':
                correctLine += line[j]

        lines[i] = correctLine

    if assertFormatLoad():
        for line in lines:
            print("\t" + line)
        print(f'\n\t{len(lines)} new rule(s) added')
    else:
        print(f'Error! {fileName} is not a valid knowledge base')


##
# AssertFormat function check if the KB is in correct format
# Also splits all the atom and appends them to the list of data
def assertFormatLoad():
    for line in lines:
        splitHead = line.split(' <-- ')
        if len(splitHead) != 2:
            return False

        head = splitHead[0]
        splitAtoms = splitHead[1]
        splitAtoms = splitAtoms.split(' & ')

        for atom in splitAtoms:
            if is_atom(atom) is False:
                return False

        newData = [head, splitAtoms]  # Create a list of atoms on the line
        data.append(newData)  # Append that list to the existing database

    return True


"""_______________________________________________TELL________________________________________________"""


def tell(command):
    temp = ""

    for i in range(len("tell "), len(command)):
        temp += command[i]

    splitCommand = temp.split()  # Default split is with ' '

    if not assertFormatTell(splitCommand):
        print("Tell failed!")
        return
    newKb = []  # check atoms added within this command
    checked = []  # check atoms already checked (to void repetition of print statements)

    for rule in data:
        for elt in splitCommand:
            if elt in rule[0] or elt in rule[1]:
                if elt in KB:
                    if elt not in newKb and elt not in checked:
                        print(f'\tatom "{elt}" already known to be true')
                        checked.append(elt)
                else:
                    KB.append(elt)
                    newKb.append(elt)
                    print(f'\t"{elt}" added to KB')

    return


def assertFormatTell(atoms):
    if atoms == "" or atoms == " ":
        print(f'Error! Empty command not acceptable')
        return False

    for atom in atoms:
        if not is_atom(atom):
            print(f'Error! "{atom}" is not a valid atom')
            return False

    return True


"""____________________________________________INFER-ALL__________________________________________________"""


def infer_all():
    global inferred
    inferred = []
    for rule in data:
        temp = []
        for atom in rule[1]:
            if rule[0] not in KB and rule[0] not in inferred:
                if atom in KB:
                    temp.append(atom)
        if temp == rule[1]:
            inferred.append(rule[0])

    return inferred


"""____________________________________________CHECK_ATOM_________________________________________________"""


# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])


def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"


"""____________________________________________INTERPRETER_________________________________________________"""

##
# Check if command is valid or not
def isValid(command):
    for st in listOfCommands:
        if st in command:
            return st
    return None


##
# Interpreter Function
def interpreter():
    command = input("kb> ")
    valid = isValid(command)
    if valid is not None:
        if valid == "load":
            load(command)
            return
        elif valid == "tell":
            tell(command)
            return
        elif valid == "infer_all":
            global inferred
            inferTemp = infer_all()
            for atom in inferTemp:
                KB.append(atom)

            keepGoing = True
            while keepGoing:
                temp = infer_all()
                if len(temp) == 0:
                    keepGoing = False
                else:
                    for elt in temp:
                        inferTemp.append(elt)
                        KB.append(elt)
            inferred = inferTemp
            printValues()
            return
    else:
        print(f'Error: unknown command {command}')
        return


##
# Print function for values in infer_all() in interpreter function
def printValues():
    print(f'\tNewly inferred atoms:')
    if len(inferred) == 0:
        print("\t   <none>")
    else:
        printInferred()

    print(f'\tAtoms already known to be true:')
    if len(KB) == 0:
        print("\t   <none>")
    else:
        printKB()


def printInferred():
    print("\t", end="   ")
    for i in range(len(inferred)):
        if i == len(inferred) - 1:
            print(f'{inferred[i]}')
        else:
            print(f'{inferred[i]}', end=", ")
    return


def printKB():
    print("\t", end="   ")
    for i in range(len(KB)):
        if KB[i] not in inferred:
            if i == 0:
                print(f'{KB[i]}', end="")
            else:
                print(f', {KB[i]}', end="")
    print("")
    return


"""____________________________________________RUN PROGRAM_________________________________________________"""


# Infinitely running interpreter
def run():
    stop = False
    while stop is False:
        interpreter()


if __name__ == '__main__':
    run()
