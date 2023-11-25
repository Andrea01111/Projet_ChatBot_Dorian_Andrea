# Import functions from the "Functionality" file
from functionality import *
import time

# Create a list for each number of functionalities
L=['1','2','3','4','5','6']

# Verify if it is the correct file to execute the code
if __name__ == '__main__':
    rep = True

    print("Bienvenue sur le menu de notre chatbot")
    print("Vous pouvez demander d'accéder à un certain nombre de fonctionnalités")
    # Ask the user if he wants to have access to functionalities or quit the menu
    print("Souhaitez vous accéder aux fonctionnalités ? oui/non")
    a = input()
    # Security if the user didn't respond as expected
    while a != 'oui' and a != 'non':
        print("Vous ne pouvez répondre à cette question seulement par 'oui' ou par 'non'")
        a = input()
    # Introduce each functionalities associated with a number
    if a == 'oui':
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
        print("(6) Vous pouvez demander tous les mots que la totalité des présidents ont prononcés dans leur discours")
        time.sleep(1)
        print()

        # Ask which functionality he wants by a number
        while rep:
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
            # Functionality n°6
            if nb == '6':
                print()
                print(higher_f_words())
                print("Il s'agit des mots similaires évoqués par tous les présidents dans les discours hormis ceux considérés comme 'non importants'")
                print()

            # Ask if the user wants to continue or quit the menu
            print("Vous pouvez sortir du menu si vous saisissez 'stop' sinon 'continuer'")
            str = input()
            # Security if the user didn't respond by "stop" or "continuer"
            while str != 'stop' and str!= 'continuer':
                print("Veuillez saisir 'stop' ou 'continuer'")
                str = input()
            # Close the menu if the user wrote "stop"
            if str == 'stop':
                print()
                print()
                print("Fermeture du menu")
                rep = False

    # Close the menu if the user has written "non" at the first question
    print()
    print()
    print("Fermeture du programme")


