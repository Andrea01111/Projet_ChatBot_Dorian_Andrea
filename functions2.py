from functions import *
import functionality
import math
import os


def token(txt):
    """
    :param txt: takes the request : string
    :return: return the word of the question split by " " : l
    """
    nw_txt = ""
    l = []
    #Loop to remove the capital letter and the punctuation
    for i in txt:
        if 65 <= ord(i) <= 90 or 192 <= ord(i) <= 223:
            nw_txt += chr(ord(i)+32)
        elif 97 <= ord(i) <= 122 or 224 <= ord(i) <= 255:
            nw_txt += i
        else:
            nw_txt += " "
    l_inter = nw_txt.split(" ")
    #Loop to delete all the non-words
    for i in range(len(l_inter)):
        if len(l_inter[i]) > 1:
            l.append(l_inter[i])
    return l


def word_in_corpus(txt):
    """
    :param txt: takes the token question : string
    :return: return a list with the words of the question that occurs in the corpus.
    """
    l_corpus = tf_1()[0]
    l1 = token(txt)
    l2 = []
    #loop to navigate in the token question
    for i in range(len(l1)):
        if l1[i] in l_corpus:
            l2.append(l1[i])
    return l2


def tf_idf_question(txt):
    """
    :param txt: request from the user : string
    :return: return a dictionary with the word from the corpus : d_tf_idf = {"word": tf_idf score}
    """
    l1 = token(txt)
    l2 = word_in_corpus(txt)
    l3 = tf_1()[0]
    d_tf = {}
    d_idf = idf()
    d_tf_idf = {}
    #Loop to make the tf score for each word from the question and put them in a dictionary
    for i in range(len(l1)):
        cpt = 0
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                cpt += 1
        d_tf[l1[i]] = cpt
    #Loop to put the tf-IDF score in the dictionary d_tf_idf
    for i in range(len(l3)):
        if l3[i] in d_tf.keys():
            d_tf_idf[l3[i]] = d_tf[l3[i]]*d_idf[l3[i]]
        else:
            d_tf_idf[l3[i]] = 0
    return d_tf_idf


def transpose(M):
    """
    :param M: Matrix
    :return: transpose of matrix
    """
    MT = []
    # Loop in the matrix
    for i in range(len(M[0])):
        l = []
        for j in range(len(M)):
            #inverse of the index
            l.append(M[j][i])
        MT.append(l)
    return MT


def p_scalar(q_tf_idf,M_tf_idf):
    """
    :param q_tf_idf:  dictionary of the tf_idf score of the request
    :param M_tf_idf:  transpose of the matrix tf_idf score
    :return: d1 = { "name of the document": p_scalar}
    """
    d1 = {}
    # loop to navigate in the lign of the matrix
    for i in range(1,len(M_tf_idf)):
        s = 0
        #loop to navigate in the column of the matrix
        for j in range(1,len(M_tf_idf[0])):
            s += M_tf_idf[i][j]*q_tf_idf[M_tf_idf[0][j]]
        d1[M_tf_idf[i][0]] = s
    return d1


def norm(a):
    """
    :param a: vector
    :return: the norm of a vector (float)
    """
    n = 0
    #Condition if the vector is a dictionary
    if type(a) == dict:
        for value in a.values():
            n += value**2
        n = math.sqrt(n)
    #Condition if the vector is a list
    elif type(a) == list:
        for i in range(1,len(a)):
            n += a[i]**2
        n = math.sqrt(n)
    return n


def similarity(q_tf_idf,M_tf_idf):
    """
    :param q_tf_idf: tf_idf question vector
    :param M_tf_idf: transpose of the tf_idf matrix
    :return: d_similarity = {"name of the file" : cos similarity (float)}
    """
    d_similarity = {}
    d_p_scalar = p_scalar(q_tf_idf,M_tf_idf)
    # loop to navigate in the matrix transpose
    for i in range(1,len(M_tf_idf)):
        d_similarity[M_tf_idf[i][0]] = d_p_scalar[M_tf_idf[i][0]]/(norm(q_tf_idf)*norm(M_tf_idf[i]))
    return d_similarity


def doc_simil(d):
    """
    :param d: similarity dictionary : d = {"name of the file" : cos similarity (float)}
    :return: string of the file with the higher cos similarity score
    """
    doc = ""
    maxi = 0
    #Loop to navigate in the dictionary
    for keys,val in d.items():
        #Select the maximum
        if val > maxi:
            maxi = val
            doc = keys
    return doc


def answer(doc,tf_idf_q):
    """
    :param doc: string of the file with the higher cos similarity score
    :param tf_idf_q: tf_idf request vector
    :return: string : answer of the request
    """
    dir = os.getcwd()
    maxi = 0
    h_tf_idf_q = ""
    ph = ""
    l4 = functionality.lower_tf_idf()
    l5 = ["peux","comment","quel","quelle","quels","quelles","pourquoi",""," "]
    #Set the less important word in l4
    for i in range(len(l5)):
        l4.append(l5[i])
    #loop to get the higher term tf_idf score in the request vector : h_tf_idf_q
    for keys, val in tf_idf_q.items():
        if (val > maxi) and (keys not in l4):
            maxi = val
            h_tf_idf_q = keys
    # change dir to get the file
    os.chdir(dir + "/speeches-20231105")
    # opening of the file
    with open(doc,"r",encoding="UTF-8") as f:
        l1 = f.readlines()
        l2 = []
        # Loop to concatenate all the lign from the file in a string
        for i in range(len(l1)):
            st = ""
            for j in range(len(l1[i])-1):
                st += l1[i][j]
            l2.append(st)
    st_doc = ""
    # Split the lign where "." in a list
    for i in range(len(l2)):
        st_doc += l2[i]
    l3 = st_doc.split(".")
    bool = False
    i = 0
    # loop the find the first sentence of the h_tf_idf_q in l3 : ph
    while not bool:
        if h_tf_idf_q in l3[i]:
            bool = True
            ph = l3[i]
        i += 1
    os.chdir(dir)
    return ph


def p_answer(request):
    """
    :param request: takes the answer from the request
    :return: answer
    """
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"
    }
    tf__idf = tf_idf()
    tf_idf_q = tf_idf_question(request)
    ans = answer(doc_simil(similarity(tf_idf_q,transpose(tf__idf))),tf_idf_q)
    l1 = request.split(" ")
    rep = ans + "."
    #loop to select question starters
    for keys, val in question_starters.items():
        if l1[0] == keys:
            rep = val + ans.lower() + "."
    return rep
