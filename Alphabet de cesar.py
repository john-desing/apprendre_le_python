alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet2 = list('abcdefghijklmnopqrstuvwxyz')
##print (alphabet)
phrase = input("Ecrivez une phrase:")
print(phrase)
decalage = input("Valeur du decalage?")
def ceasar():
    x,y,z = 0,1,1
    while x<26:
        y = x+int(decalage)
        z = y - 26
        if(y<26):
            alphabet[x] = alphabet[y]
        else:
            alphabet[x] = alphabet2[z]
        x = x + 1
    print(alphabet)
ceasar()
newPhraseList = list(phrase)
nbLettres = len(phrase)
newPhrase = ""
n = 0
while n<nbLettres:
    newPhrase = newPhrase+""+newPhraseList[n]
    phraseFinal = newPhrase.replace(newPhraseList[n],alphabet[n])
    n = n + 1
    print (phraseFinal)