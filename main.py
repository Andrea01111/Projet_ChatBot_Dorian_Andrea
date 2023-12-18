"""MY_FIRST_CHATBOT Dorian Maury - Andrea Dario : fichier main pour l'éxecution du menu."""
# Import functions from the "Functionality" file
from functionality import *
import functions2
import time
import random
import os

# Create a list for each number of functionalities
L = ['1','2','3','4','5']
#Main path
dir = os.getcwd()

# Verify if it is the correct file to execute the code
if __name__ == '__main__':
    rep1 = True
    print("Bienvenue sur le menu de notre chatbot")
    print("Vous pouvez demander d'accéder à un certain nombre de fonctionnalités")

    # Ask the user if he wants to have access to functionalities or quit the menu
    while rep1 == True:
        print("Souhaitez vous accéder aux fonctionnalités ou au chatbot? fonctionnalités/chatbot")
        a = input()

        # Security if the user didn't respond as expected
        while a != 'fonctionnalités' and a != 'chatbot':
            print("Vous ne pouvez répondre à cette question seulement par 'fonctionnalités' ou par 'chatbot'!")
            a = input()

        # Introduce each functionalities associated with a number
        if a == 'fonctionnalités':
            rep2 = True
            print("Pour accéder aux fonctionnalités il suffit de saisir le numéro indiqué entre paranthèses au début de chaque ligne")
            print()
            time.sleep(1)
            print("Voici la liste des fonctionnalités : ")
            print()
            time.sleep(1)
            print("(1) Vous pouvez demander d'afficher la liste des mots les moins importants dans le corpus de documents ")
            time.sleep(1)
            print("(2) Vous pouvez demander d'afficher le mot ayant le score TD-IDF le plus élevé parmi tous les discours")
            time.sleep(1)
            print("(3) Vous pouvez demander le mot le plus répété par le président Chirac")
            time.sleep(1)
            print("(4) Vous pouvez demander les noms des présidents qui ont parlé de la Nation et celui qui l’a répété le plus de fois")
            time.sleep(1)
            print("(5) Vous pouvez demander le premier président qui a parlé du climat ou de l’écologie dans les différents discours")
            time.sleep(1)
            print()

            # Ask which functionality he wants by a number
            while rep2:
                nb = input("Entrer le numéro de la fonctionnalité ici : ")
                # Security if the user didn't use one of the number in the list
                while nb not in L:
                    print("Ce choix n'existe pas, veuillez réessayer")
                    nb = input("Entrer le numéro de la fonctionnalité ici : ")

                # Functionality n°1
                if nb == '1':
                    print()
                    print(lower_tf_idf())
                    print("Il s'agit des mots les moins importants dans les discours")
                    print()
                # Functionality n°2
                if nb == '2':
                    print()
                    print(max_tf_idf())
                    print("Il s'agit du mot qui possède le score TF-IDF le plus élevé")
                    print()
                # Functionality n°3
                if nb == '3':
                    print()
                    print(max_f_word('Chirac'))
                    print("Il s'agit du mot le plus prononcé par le président Chirac")
                    print()
                # Functionality n°4
                if nb == '4':
                    print()
                    print(find_word('nation'))
                    print("Il s'agit du nom de président qui a prononcé le plus de fois le mot 'nation' dans son discours ainsi que la liste des présidents qui l'ont évoqué")
                    print()
                # Functionality n°5
                if nb == '5':
                    print()
                    print(climate_eco())
                    print("Il s'agit du nom du premier président à avoir évoqué le climat ou l'écologie dans son discours")
                    print()

                # Ask if the user wants to continue or quit the menu
                print("Vous pouvez sortir des fontionnalités si vous saisissez 'stop' sinon 'continuer'")
                str = input()
                # Security if the user didn't respond by "stop" or "continuer"
                while str != 'stop' and str!= 'continuer':
                    print("Veuillez saisir 'stop' ou 'continuer'")
                    str = input()
                # Close the menu if the user wrote "stop"
                if str == 'stop':
                    print()
                    print()
                    print("Retour au menu")
                    rep2 = False
                os.chdir(dir)

        # Condition if the user chose chatbot
        elif a == "chatbot":
            rep3 = True
            print("Bienvenue sur MyEfreiBot")
            time.sleep(2)
            print("Comment puis-je vous aider ?")
            while rep3:
                print()
                q = input()
                print(functions2.p_answer(q))
                time.sleep(3)
                print()
                print(random.choice(["Avez-vous d'autres questions ?","Ravi d'avoir pu vous aidez, auriez vous d'autres questions ?","Avez-vous des questions suplémentaires à me poser ?"]))
                b = input()
                while b != "non" and b != "oui":
                    b = input("Vous pouvez seulement répondre par oui ou non")
                time.sleep(1)
                print()
                if b == "non":
                    rep3 = False
                    print("Vous quittez MyEfreiBot ...")
                else:
                    print("Très bien! Quelle est votre question ?")
                os.chdir(dir)


        time.sleep(1)
        print()
        f = input("Voulez-vous quittez le menu ?")
        while f != "non" and f != "oui":
            f = input("Vous pouvez seulement répondre par oui ou non")
        print()
        if f == "oui":
            rep1 = False
            print("Vous quittez le menu ...")
    time.sleep(2)
    # Close the menu if the user has written "non" at the first question
    print()
    print()
    print("Fermeture du programme")