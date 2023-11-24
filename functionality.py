from functions import *

def lower_tf_idf():
    M_tf_idf = tf_idf()
    l = []
    for i in range(1,len(M_tf_idf)):
        cpt = 0
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] == 0:
                cpt += 1
        if cpt == (len(M_tf_idf[i])-1):
            l.append(M_tf_idf[i][0])
    return l



def max_tf_idf():
    M_tf_idf = tf_idf()
    l = []
    maxi = 0
    for i in range(1,len(M_tf_idf)):
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] > maxi:
                maxi = M_tf_idf[i][j]
    for i in range(1,len(M_tf_idf)):
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] == maxi:
                l.append(M_tf_idf[i][0])
    return l


def max_f_word(txt):
    M_tf_ocu = tf_2()[1]
    l = []
    l2 = []
    maxi = 0
    for i in range(len(M_tf_ocu[0])):
        if txt in M_tf_ocu[0][i]:
            l.append(i)
    for i in range(len(l)):
        for j in range(1,len(M_tf_ocu)):
            if M_tf_ocu[j][l[i]] > maxi:
                maxi = M_tf_ocu[j][l[i]]
    for i in range(len(l)):
        for j in range(1,len(M_tf_ocu)):
            if M_tf_ocu[j][l[i]] == maxi:
                l2.append(M_tf_ocu[j][0])
    return l2


def find_word(txt):
    # Init des variables
    dir = os.getcwd()
    l_name = nom_president(os.listdir(dir + "/cleaned"))
    M_tf_ocu = tf_2()[1]
    l1 = []             #Liste['name_file.txt'] des président ayant prononcé le mot
    dic = {}            #Dictionnaire avec le ou les président ayant répéter le plus de mot le mot--> {name:int}
    l_president = []            #liste['name_file.txt'] du ou des président ayant répéter le plus de fois le mot
    ind_l = 0
    maxi = 0
    l = []              #Liste['name'] des président ayant prononcé le mot
    #On récupère la ligne du mot à trouver(ind_l) et l'indice du mot le plus répéter(maxi)
    for i in range(len(M_tf_ocu)):
        if M_tf_ocu[i][0] == txt:
            maxi = M_tf_ocu[i][1]
            ind_l = i
            for j in range(2,len(M_tf_ocu[i])):
                if M_tf_ocu[i][j] > maxi:
                    maxi = M_tf_ocu[i][j]
    #On récupère le ou les président ayant répéter le plus de fois le mot. L1 liste du ou des président ayant répéter
    #le plus de fois. l1 liste du tout les président ayant répéter
    for i in range(1,len(M_tf_ocu[ind_l])):
        if M_tf_ocu[ind_l][i] == maxi:
            l_president.append(M_tf_ocu[0][i])
        if M_tf_ocu[ind_l][i] > 0:
            l1.append(M_tf_ocu[0][i])
    # On affecte le ou les président qui a répéter le plus de fois le mot dans un dictionnaire et ceux qui l'on évoqué
    # dans une liste
    for i in range(len(l_name)):
        for j in range(len(l_president)):
            if l_name[i] in l_president[j]:
                dic[l_name[i]] = maxi
        for j in range(len(l1)):
            if l_name[i] in l1[j]:
                l.append(l_name[i])
    l = list(set(l))
    return dic,l


def climate_eco():
    dir = os.getcwd()
    l_name = nom_president(os.listdir(dir + "/cleaned"))
    M_tf_ocu = tf_2()[1]
    bool = True
    ind = 0
    for i in range(len(M_tf_ocu)):
        if M_tf_ocu[i][0] == "climat" or M_tf_ocu[i][0] == "écologie":
            for j in range(1,len(M_tf_ocu[i])):
                if M_tf_ocu[i][j] != 0 and bool == True:
                    bool = False
                    ind = j
    str_pre = M_tf_ocu[0][ind]
    for i in range(len(l_name)):
        if l_name[i] in str_pre:
            str_pre = l_name[i]
    return str_pre

print(climate_eco())


def higher_f_words():
    M_tf_ocu = tf_2()[1]
    l = []
    for i in range(1,len(M_tf_ocu)):
        bool = True
        for j in range(1,len(M_tf_ocu[i])):
            if M_tf_ocu[i][j] == 0:
                bool = False
        if bool:
            l.append(M_tf_ocu[i][0])
    return l

