import sys
import cv2 as cv
from fingerprint import *
from voiceR import *


def main() -> None:
    print("Welcome to system!")
    newUserFlag = input("Are you a new user?\n0 - yes\n1 - no\nAnswer:\t")

    if (newUserFlag == '0'):
        name = input("Please provide your name:\t")
        gender = input("Please provide your gender (m / f):\t")
        fingerPrintFile = input("Please provide your fingerprint file:\t")
        voiceFile = input("Please provide your voice file sample:\t")

        f = open("database.txt", 'r')

        # Check for user in database
        lines = f.readlines()
        flagFPinDB = False
        flagVinDB = False
        for line in lines:
            if (line.split(',')[2] == fingerPrintFile):
                flagFPinDB = True
            if (line.split(',')[3] == voiceFile):
                flagVinDB = True
        f.close()

        if (flagFPinDB or flagVinDB):
            if (flagFPinDB):
                print("Fingerprint already in database!")
            if (flagVinDB):
                print("Voice sample already in database!")
            sys.exit(1)

        f = open("database.txt", 'w')
        f.write(name + "," + gender + "," + fingerPrintFile + "," + voiceFile)
        f.close()

        print("User added successfully!")
        sys.exit(0)

    # Check for existing user
    name = input("Please provide your name:\t")

    # Check for user in database
    f = open("database.txt", 'r')
    lines = f.readlines()
    flagUser = False
    for line in lines:
        if (line.split(',')[0] == name):
            flagUser = True
    f.close()
    if (not flagUser):
        print("Name is not in the database!")
        sys.exit(1)

    fingerPrintFile = input("Please provide your fingerprint file:\t")
    fpUnlocked, fpFilename = fingerprint(fingerPrintFile)

    if (not fpUnlocked):
        print("User is not validated, fingerprint didn't matched database!")
        sys.exit(1)

    # Check for user in database
    f = open("database.txt", 'r')
    flagFP = False
    for line in f.readlines():
        if (line.split(',')[2] == fpFilename):
            flagFP = True
    f.close()
    if (not flagFP):
        print("Fingerprint is wrong!")
        sys.exit(1)
    else:
        print("User is validated, fingerprint matched the one in our database!")

    voiceFile = input("Please provide your voice file:\t")
    gender = voice(voiceFile)
    f = open("database.txt", 'r')
    flagV = False
    for line in f.readlines():
        if (line.split(',')[1] == gender):
            flagV = True
    f.close()

    if (not flagV):
        print("User is not validated, gender of the voice didn't matched the declared one!")
        sys.exit(1)

    print("You may enter!")
    sys.exit(0)


if __name__ == "__main__":
    main()