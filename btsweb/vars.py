import random

def makeUcode():
    alpahbet = "abcdefghijklmnopqrstuvwxyz0123456789"
    Ucode = ""
    
    for i in range(6):
        index = random.randrange(len(alpahbet))
        Ucode = Ucode + alpahbet[index]
    return Ucode