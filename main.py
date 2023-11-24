from functionality import *
import time
L=['1','2','3','4','5','6']

if __name__ == '__main__':
    rep = True

    print("Bienvenue sur le menu de notre chatbot")
    print("Vous pouvez demander d'accéder à un certain nombre de fonctionnalités")
    print("Souhaitez vous accéder aux fonctionnalités ? oui/non")
    a = input()
    while a != 'oui' and a != 'non':
        print("Vous ne pouvez répondre à cette question seulement par 'oui' ou par 'non'")
        a = input()
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

        while rep:
            nb = input("Entrer le numéro de la fonctionnalité ici : ")
            while nb not in L:
                print("Ce choix n'existe pas, veuillez réessayer")
                nb = input("Entrer le numéro de la fonctionnalité ici : ")

            if nb == '1':
                print()
                print(lower_tf_idf())
                print("Il s'agit des mots les moins importants dans les discours")
                print()
            if nb == '2':
                print()
                print(max_tf_idf())
                print("Il s'agit du mot qui possède le score TF-IDF le plus élevé")
                print()
            if nb == '3':
                print()
                print(max_f_word('Chirac'))
                print("Il s'agit du mot le plus prononcé par le président Chirac")
                print()
            if nb == '4':
                print()
                print(find_word('nation'))
                print("Il s'agit du nom de président qui a prononcé le plus de fois le mot 'nation' dans son discours ainsi que la liste des présidents qui l'ont évoqué")
                print()
            if nb == '5':
                print()
                print(climate_eco())
                print("Il s'agit du nom du premier président à avoir évoqué le climat ou l'écologie dans son discours")
                print()
            if nb == '6':
                print()
                print(higher_f_words())
                print("Il s'agit des mots similaires évoqués par tous les présidents dans les discours hormis ceux considérés comme 'non importants'")
                print()

            print("Vous pouvez sortir du menu si vous saisissez 'stop' sinon 'continuer'")
            str = input()
            while str != 'stop' and str!= 'continuer':
                print("Veuillez saisir 'stop' ou 'continuer'")
                str = input()
            if str == 'stop':
                print()
                print()
                print("Fermeture du menu")
                rep = False

    print()
    print()
    print("Fermeture du programme")


