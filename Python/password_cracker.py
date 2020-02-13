# Explanation :  Load the hashes from the passwd file.
# For brute force, create a recursive loop to generate word lists.
# Whether it's brute force or dictionary, iterate over the list of strings.
# Calculate MD5 hashes of each string and compare with the hashes from the passwd file.

import hashlib
import string
import sys
import argparse

# Store the hash digests
hash_digests = []


# Calculate MD5 value
def calcMD5(i):
    return hashlib.md5(i.strip().encode("utf-8")).hexdigest()
    # Strip to remove new lines and convert to hex digest.


# Load hashes from the file
def loadHashes(filename):
    global hash_digests
    with open(filename, "r") as f:
        for i in f.readlines():
            hash_digests.append(i.strip())
    if len(hash_digests) != 0:
        print("Hashes Loaded")
    else:
        print("No hashes found in the specified file.\nEnter a valid file")
        sys.exit(0)


def generate(l, d):
    if d < 1:
        return
    for c in l:
        if d == 1:
            yield c
        else:
            for k in generate(l, d - 1):
                yield c + k


# Brute force function
def bruteforce(list, count):
    global hash_digests
    for d in range(1, count + 1):
        for c in generate(list, d):
            m = calcMD5(c)
            if m in hash_digests:
                print("Password Cracked \nHash: {0} Password {1}".format(m, c))
                hash_digests.remove(m)
            if len(hash_digests) == 0:
                print("All Passwords Cracked")
                sys.exit(0)  # Exit the loop in case all hashes are found


def dictionaryAttack(filename):
    global hash_digests
    with open(filename, "r") as f:
        for i in f.readlines():
            m = calcMD5(i)
            if m in hash_digests:
                print("Password Cracked \nHash: {0} Password {1}".format(m, i))
                hash_digests.remove(m)
            if len(hash_digests) == 0:
                print("All Passwords Cracked")
                sys.exit(0)  # Exit the loop in case all hashes are found


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--hash-file", help="Load Hash File", required=True)
    parser.add_argument("-d", "--dictionary-file", help="Load Dictionary File")
    parser.add_argument("-b", "--brute-force", help="Choose an option\n1. Lower case\n2. Upper case\n3. Digits\n4. All")
    args = vars(parser.parse_args())
    hashfile = args["hash_file"]
    brute_force = args["brute_force"]
    dictionary = args["dictionary_file"]
    loadHashes(hashfile)
    if brute_force:
        if brute_force == "1":
            bruteforce(string.ascii_lowercase, 6)  # a-z
        elif brute_force == "2":
            bruteforce(string.ascii_uppercase, 6)  # A-Z
        elif brute_force == "3":
            bruteforce(string.digits, 6)  # 0-9
        elif brute_force == "4":
            bruteforce(string.digits + string.ascii_letters + string.punctuation,
                       6)  # string.punctuation includes symbols
        else:
            print("Unknown Option")
    elif dictionary:
        dictionaryAttack(dictionary)
    else:
        print("Choose either brute force or dictionary attack")
