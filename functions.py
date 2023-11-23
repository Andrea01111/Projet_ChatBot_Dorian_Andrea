import os
import time
import math

print()

def makedir(txt):
    os.mkdir(txt)
    print(f"Making of the directory '{txt}'... ")
    time.sleep(1)
    return ""


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Call of the function
directory = 'speeches-20231105'
files_names = list_of_files(directory, "txt")
#print(files_names)

def nom_president(file_names):
    l_of_names = []
    for i in range(len(file_names)):
        s = ''
        for j in range(11,len(file_names[i])-4):
            st = ord(file_names[i][j])
            if 90 >= st >= 65 or 122 >= st >= 97:
                s += file_names[i][j]
        l_of_names.append(s)
    return list(set(l_of_names))

l_name_president = nom_president(files_names)
#print(l_name_president)

def first_name():
    global l_name_president
    dic_first_name = {}
    for i in range(len(l_name_president)):
        dic_first_name[l_name_president[i]] = input(f"Enter the first name of {l_name_president[i]} : ")
    return dic_first_name

def show_president():
    global l_name_president
    for i in range(len(l_name_president)):
        print(l_name_president[i],end=" ")
    return ""

def cleaned_file(text):
    dir = os.getcwd()
    #Creation of repertory "cleaned" if he doesn't exist
    if "cleaned" not in os.listdir(dir):
        makedir("cleaned")
    #Verification if the file request doesn't exist already
    if text in os.listdir(dir + "/cleaned"):
        return f"The file '{text}' already exist in 'cleaned'"
    else:
        #Beginning of the function ( change all capital letter to lowercase letter)
        os.chdir(dir + "/speeches-20231105")
        with open(text,"r",encoding="UTF-8") as t:
            l = t.readlines()
            new_txt = ""
            for i in range(len(l)):
                new_st = ""
                for j in range(len(l[i])):
                    string = l[i][j]
                    if 90 >= ord(l[i][j]) >= 65 or 223 >= ord(l[i][j]) >= 192:
                        string = chr(ord(l[i][j]) + 32)
                    new_st += string
                new_txt += new_st
    os.chdir(dir + '/cleaned')
    print(f"Making of the file '{text}' in 'cleaned'...")
    time.sleep(1)
    with open(text,"w",encoding="UTF-8") as c:
        c.write(new_txt)
    os.chdir(dir)
    return ""


#print(cleaned_file("Nomination_Mitterrand1.txt"))


def del_punctuation(text):
    dir = os.getcwd()
    if "cleaned" not in os.listdir(dir):
        cleaned_file(text)
    elif text not in os.listdir("cleaned"):
        cleaned_file(text)
    os.chdir(dir + "/cleaned")
    t = open(text,"r",encoding="UTF-8")
    txt = t.readlines()
    t.close()
    t = open(text,"w", encoding="UTF-8")
    new_txt = ""
    for i in range(len(txt)):
        st = ""
        for j in range(len(txt[i])):
            if 122 >= ord(txt[i][j]) >= 97 or 255 >= ord(txt[i][j]) >= 224 or txt[i][j] == " ":
                st += txt[i][j]
            elif (txt[i][j] == "'" or txt[i][j] == "-") and j != 0:
                st += " "
            elif txt[i][j] == "\n":
                st += "\n"
        new_txt += st
    t.write(new_txt)
    t.close()
    os.chdir(dir)
    return ""

#print(del_punctuation("Nomination_Sarkozy.txt"))


def del_punctuation_all_file():
    dir = os.getcwd()
    l = os.listdir(dir + "/speeches-20231105")
    for i in range(len(l)):
        #MacOS condition
        if l[i] != '.DS_Store':
            del_punctuation(l[i])
    return ""


#del_punctuation_all_file()


#Creation of the list with the unique words and a
#dictionary {"name of file": [] list with all the words within the file}
def tf_1():
    # Initiating variables
    dir = os.getcwd()
    if "cleaned" not in os.listdir(dir):
        del_punctuation_all_file()
    l_file = list_of_files("cleaned", "txt")
    s_words = ""
    l_words = []
    dic_l_file = {}
    # Change of repertory
    os.chdir(dir + "/cleaned")
    #Loop to open and manipulate all files
    for i in range(len(l_file)):
        #String which will become a list to add to the dictionary
        s = ""
        with open(l_file[i],"r", encoding="UTF-8") as t:
            l_t = t.readlines()
            dic_l_file[l_file[i]] = []
            for j in range(len(l_t)):
                # Condition to avoid the string " " in the beginning of the lign
                # and suppression of the character with length 1 and "\n" at the end of the lign
                if l_t[j][0] != " ":
                    txt = l_t[j][0]
                    for k in range(len(l_t[j])):
                        if 0 < k < len(l_t[j])-1:
                            if l_t[j][k-1] != " " or l_t[j][k+1] != " ":
                                txt += l_t[j][k]
                    txt += " "
                else:
                    txt = ""
                    for k in range(1,len(l_t[j])):
                        if k < len(l_t[j])-1:
                            if l_t[j][k - 1] != " " or l_t[j][k+1] != " ":
                                txt += l_t[j][k]
                    txt += " "
                s_words += txt
                s += txt
            #Separation of the words and deletion of the string "" in the list for the dictionary
            s = s.split(" ")
            for x in range(len(s)):
                if s[x] != "":
                    dic_l_file[l_file[i]].append(s[x])
    # Separation of the words and deletion of the string "" in the list of unique words
    l = s_words.split(" ")
    for i in range(len(l)):
        if l[i] != "":
            l_words.append(l[i])
    os.chdir(dir)
    return list(set(l_words)),dic_l_file


def tf_2():
    l_uni = tf_1()[0]
    dic = tf_1()[1]
    M_tf = [["words"]]
    M_ocu = [["words"]]
    #Initiating of the first lign in M_tf/M_ocu
    for keys in dic.keys():
        M_tf[0].append(keys)
        M_ocu[0].append(keys)
    # Matrix for a term frequency in a document
    for i in range(len(l_uni)):
        l_inter_tf = [l_uni[i]]
        l_inter_ocu = [l_uni[i]]
        for val in dic.values():
            cpt = 0
            for j in range(len(val)):
                if l_uni[i] == val[j]:
                    cpt += 1
            l_inter_tf.append(cpt/len(val))
            l_inter_ocu.append(cpt)
        M_tf.append(l_inter_tf)
        M_ocu.append(l_inter_ocu)
    return M_tf,M_ocu


#Function to show matrix TF, takes TF matrix in parameter
def show_tf(M):
    l_uni = tf_1()[0]
    maxi = l_uni[0]
    for i in range(len(l_uni)):
        if len(l_uni[i]) > len(maxi):
            maxi = l_uni[i]
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="\t")
        print()
    return ""

#show_tf(tf_2()[1])

def idf():
    M = tf_2()[1]
    dir = os.getcwd()
    len_file = len(os.listdir(dir + "/cleaned"))
    dic_idf = {}
    for i in range(1,len(M)):
        cpt = 0
        for j in range(1,len(M[i])):
            if M[i][j] > 0:
                cpt += 1
        dic_idf[M[i][0]] = math.log(len_file/cpt)
    return dic_idf



#Ctabet93
#guiras.zouhour@gmail.com