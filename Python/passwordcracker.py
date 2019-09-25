import hashlib
import binascii
import string
import sys

# str = "Jason:502:aad3c435b514a4eeaad3b935b51304fe:c46b9e588fa0d112de6f59fd6d58eae3:::"
# #
# # 0 - Username
# # 1 - Relative administrator
# # 2 - LM hash
# # 3 - NT Hash
# print(str.split(":"))

# Hashing Functions
def calculateNTLMHash(str):
    hash = hashlib.new('md4', str.encode('utf-16le')).digest()
    return binascii.hexlify(hash)

def calculateMD5Hash(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()

def calculateSHA256Hash(str):
    return hashlib.sha256(str.encode("utf-8")).hexdigest()

def calculateSHA512Hash(str):
    return hashlib.sha512(str.encode("utf-8")).hexdigest()

#If no password file is given, generate a word list.
def generateWordlist(charSet,minRange=1,maxRange=8):
    wordList = []
    for current in range(minRange,maxRange):
        a = [i for i in charSet]
        for y in range(current):
            a = [x+i for i in charSet for x in a]
        wordList = wordList+a
    return wordList

def crackPassword(wordList,hash, hashingMethod):
    if hashingMethod == "sha512":
        return crackPasswordWith(calculateSHA512Hash,wordList,hash)
    elif hashingMethod == "sha256":
        return crackPasswordWith(calculateSHA256Hash,wordList,hash)
    elif hashingMethod == "md5":
        return crackPasswordWith(calculateMD5Hash,wordList,hash)
    elif hashingMethod == "ntlm":
        return crackPasswordWith(calculateNTLMHash,wordList,hash)
    else:
        return None

def crackPasswordWith(hashingFuction,wordList,hash):
    for i in wordList:
        if(hashingFuction(i) == hash):
            return i

#Check whether password file is given and also check whether it exists.
def isPasswordFileGiven():
    try:
        return (sys.argv[1] is not None)
    except:
        return False

if __name__ == '__main__':
    if(not isPasswordFileGiven()):
        wordList = generateWordlist(string.ascii_lowercase,maxRange=2)
        print(crackPassword(wordList,calculateNTLMHash("zz"),"12"))
