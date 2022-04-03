import os.path
import sys
import src.languages as languages



# the different colors for terminal to show code difference
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKRED = '\033[1;31m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# checking if the files and command passed are valid
def check():
    if len(sys.argv) == 3:
        if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]):
            print("check the file names and try again!")
            sys.exit()
    else:
        print("invalid command")
        print("usage : python showcodediff.py <file1> <file2>")
        sys.exit()

check()


# will return the file name if the file extension is valid else it will return undefined file
def guessLang():
    return (languages.langs[sys.argv[1].split(".")[1]] + " File") if sys.argv[1].split(".")[1] in languages.langs else "undefined file"
    



def maxgap(f):
    gap = 0

    for i in range(len(f)):
        if len(f[i]) > gap:
            gap = len(f[i])

    return gap



def fillGap(l1, l2):
    if len(l1) > len(l2):
        for i in range(len(l1) - len(l2)):
            l2+=" "
            return [l1, l2]
    elif len(l2) > len(l1):
        for i in range(len(l2) - len(l1)):
            l1+=" "
            return [l1, l2]
    elif len(l2) == len(l1):
        return [l1, l2]



# getting file contents
def getFileContents():
    with open(sys.argv[1], 'r') as f1:
        file1Cont = f1.read().splitlines()

    with open(sys.argv[2], 'r') as f2:
        file2Cont = f2.read().splitlines()
    
    if len(file1Cont) > len(file2Cont):
        for i in range(len(file1Cont) - len(file2Cont)):
            file2Cont.append("")
    else:
        for i in range(len(file2Cont) - len(file1Cont)):
            file1Cont.append("")

    return [file1Cont, file2Cont]



file1Cont, file2Cont = getFileContents()


maxGap = " "*(40+maxgap(file1Cont))

print("\n")
print(bcolors.OKBLUE  + guessLang() + bcolors.ENDC + " : ")

def showDiff():
    for i in range(len(file1Cont)):
        f1 = ""
        f2 = ""

        if file1Cont[i] != file2Cont[i]:
            f2 += bcolors.OKRED + file2Cont[i] + bcolors.ENDC
        elif file1Cont[i] == file2Cont[i]:
            f2 += bcolors.OKGREEN + file2Cont[i] + bcolors.ENDC

        # this is the equation for keeping the both file lines at same line by their text length without breaking
        print(str(i + 1)+". " + bcolors.OKGREEN + file1Cont[i] + bcolors.ENDC, end = " " * (len(maxGap)-len(file1Cont[i])))
        print(str(i + 1)+". " + f2)

showDiff()
