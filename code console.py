import random

#liste stokantle nom de chaque fruits
fruits=['orange',"cerise",'annas','pasteque','pomme_dore']
#probabilité de des fruits
proba_fruits = [40,25,20,10,5]
fruits_dict ={
    "orange":5,"cerise":15,"pastecque":50,"pomme_dore":100
}

#fruit_hasard = random.choices(fruits,k=3)
#print("fruit:{}-{}-{}".format( fruit_hasard [0],fruit_hasard [1],fruit_hasard [2]))

choix_fruits= random.choices(fruits,proba_fruits,k=3)
print(choix_fruits[0],choix_fruits[1],choix_fruits[2])
#verifier les les fruits:
if choix_fruits[0]== choix_fruits[1]==choix_fruits[2] :#  si les trois fuits sont identique
    jetons=fruits_dict[choix_fruits[0]]
#if choix_fruits
    print("les trois colonne sont complétées par ",choix_fruits[0]," vo us avez gagnier " ,jetons," jetonns de plus")