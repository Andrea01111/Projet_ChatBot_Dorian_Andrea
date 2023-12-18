"""MY_FIRST_CHATBOT Dorian Maury - Andrea Dario : fichier qui comprend toutes les fonctions des fonctionnalités."""
from functions import *

#Function to get the lower tf_idf
def lower_tf_idf():
    #Initiation of variables
    M_tf_idf = tf_idf()
    l = []
    #Loop to increment a counter when the value = 0
    for i in range(1,len(M_tf_idf)):
        cpt = 0
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] == 0:
                cpt += 1
        #Condition to append the lign where the tf_idf is 0 in all file
        if cpt == (len(M_tf_idf[i])-1):
            l.append(M_tf_idf[i][0])
    return l


#Function to get the higher tf_idf score in corpus
def max_tf_idf():
    # Initiation of variables
    M_tf_idf = tf_idf()
    l = []
    maxi = 0
    #Loop to set maxi to the higher tf_idf score
    for i in range(1,len(M_tf_idf)):
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] > maxi:
                maxi = M_tf_idf[i][j]
    #Loop to append the word with the higher tf_idf score
    for i in range(1,len(M_tf_idf)):
        for j in range(1,len(M_tf_idf[i])):
            if M_tf_idf[i][j] == maxi:
                l.append(M_tf_idf[i][0])
    return l


#Function to get the most repeated term by a president
def max_f_word(txt):
    # Initiation of variables
    M_tf_ocu = tf_2()[1]
    l = []
    l2 = []
    maxi = 0
    #Loop to get the column of the name to find
    for i in range(len(M_tf_ocu[0])):
        if txt in M_tf_ocu[0][i]:
            l.append(i)
    #Loop to navigate in the column selected
    for i in range(len(l)):
        #Loop to set a maximum
        for j in range(1,len(M_tf_ocu)):
            if M_tf_ocu[j][l[i]] > maxi:
                maxi = M_tf_ocu[j][l[i]]
    #Loop to append the most repeated word by a president in the list l2
    for i in range(len(l)):
        for j in range(1,len(M_tf_ocu)):
            if M_tf_ocu[j][l[i]] == maxi:
                l2.append(M_tf_ocu[j][0])
    return l2


#Function to find a word and return a dictionary with the person who said it the most/ a list with the names who said it
def find_word(txt):
    #Initiation of variables, l1 : list['name_file.txt'], l2 : list['name'], dic : {name:int} name of the president who
    # said it the most,l_president : ['name_file.txt']
    dir = os.getcwd()
    l_name = nom_president(os.listdir(dir + "/cleaned"))
    M_tf_ocu = tf_2()[1]
    l1 = []
    l2 = []
    dic = {}
    l_president = []
    ind_l = 0
    maxi = 0
    #Loop to get the lign of the word to find (ind_l) and to set the maximum in the lign(maxi)
    for i in range(len(M_tf_ocu)):
        if M_tf_ocu[i][0] == txt:
            maxi = M_tf_ocu[i][1]
            ind_l = i
            for j in range(1,len(M_tf_ocu[i])):
                if M_tf_ocu[i][j] > maxi:
                    maxi = M_tf_ocu[i][j]
    #Loop in the lign of the word selected in parameter
    for i in range(1,len(M_tf_ocu[ind_l])):
        #Condition to append the person who said the most the word to look for in l_president
        if M_tf_ocu[ind_l][i] == maxi:
            l_president.append(M_tf_ocu[0][i])
        #Condition to append all the person who said the word in l1
        if M_tf_ocu[ind_l][i] > 0:
            l1.append(M_tf_ocu[0][i])
    #Loop to the extract name from the name_file and append it to a new list
    for i in range(len(l_name)):
        for j in range(len(l_president)):
            if l_name[i] in l_president[j]:
                dic[l_name[i]] = maxi
        for j in range(len(l1)):
            if l_name[i] in l1[j]:
                l2.append(l_name[i])
    l2 = list(set(l2))
    return dic,l2


#Function to get the first president to talk about climate or ecology
def climate_eco():
    # Initiation of variables
    dir = os.getcwd()
    l_name = nom_president(os.listdir(dir + "/cleaned"))
    M_tf_ocu = tf_2()[1]
    bool = True
    ind = 0
    #Loop to get the lign of climate or ecology, bool --> stop the loop to the first appearance of the word
    #ind --> get the column of the first president to talk about the word
    for i in range(len(M_tf_ocu)):
        if M_tf_ocu[i][0] == "climat" or M_tf_ocu[i][0] == "écologie":
            for j in range(1,len(M_tf_ocu[i])):
                if M_tf_ocu[i][j] != 0 and bool == True:
                    bool = False
                    ind = j
    str_pre = M_tf_ocu[0][ind]
    #Loop to extract the name ou of the "name_file"
    for i in range(len(l_name)):
        if l_name[i] in str_pre:
            str_pre = l_name[i]
    return str_pre
