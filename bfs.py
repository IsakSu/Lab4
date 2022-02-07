from bintreeFile import Bintree
from linkedQFile import *
alfabetslista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()           # Ett trebokstavsord per rad
        if not ordet in svenska:
            svenska.put(ordet)

def makechildren(nod, q):
    for i in range (len(nod)):
        tempstr = nod
        for j in range (len(alfabetslista)):
            #tempstr = tempstr.replace(tempstr[i], alfabetslista[j])
            tempstr = tempstr[:i] + alfabetslista[j] + tempstr[i+1:]
            if(tempstr in svenska and tempstr not in gamla and not tempstr == startord):
                gamla.put(tempstr)
                if(tempstr == slutord):
                    print("Det finns en väg till " + slutord)
                else:
                    q.enqueue(tempstr)


startord = input("Skriv in ditt första ord \n")
slutord = input("Skriv in ditt sista ord \n")
q.enqueue(startord)
while not q.isEmpty():
    nod = q.dequeue()
    makechildren(nod, q)
    if(q.isEmpty() and slutord not in gamla):
        print("Det finns inte en väg till " + slutord)
