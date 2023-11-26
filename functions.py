import os
import time
import math

#Funtion to make a directory
def makedir(txt):
    os.mkdir(txt)
    print(f"Making of the directory '{txt}'... ")
    time.sleep(1)
    return ""

#Function which will return a list of file in a directory selected
def list_of_files(directory, extension):
    files_names = []
    #Loop to navigate in the directory
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Call of the function
directory = 'speeches-20231105'
files_names = list_of_files(directory, "txt")


#Function to get the name of the president
def nom_president(file_names):
    l_of_names = []
    #Loop in the list
    for i in range(len(file_names)):
        s = ''
        #Loop in the string
        for j in range(11,len(file_names[i])-4):
            st = ord(file_names[i][j])
            #Condition to make sure the character is a letter
            if 90 >= st >= 65 or 122 >= st >= 97:
                s += file_names[i][j]
        l_of_names.append(s)
    return list(set(l_of_names))

l_name_president = nom_president(files_names)

#Function to select the first name of the president
def first_name():
    global l_name_president
    dic_first_name = {}
    for i in range(len(l_name_president)):
        dic_first_name[l_name_president[i]] = input(f"Enter the first name of {l_name_president[i]} : ")
    return dic_first_name

#Function to print the name of the president
def show_president():
    global l_name_president
    for i in range(len(l_name_president)):
        print(l_name_president[i],end=" ")
    return ""


#Function to delete all the capital letter and to create a new directory to put them in
def cleaned_file(text):
    dir = os.getcwd()
    #Creation of repertory "cleaned" if he doesn't exist
    if "cleaned" not in os.listdir(dir):
        makedir("cleaned")
    #Verification if the file request, doesn't exist already
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
    #Writting of the file
    with open(text,"w",encoding="UTF-8") as c:
        c.write(new_txt)
    os.chdir(dir)
    return ""


#Function to delete all punctuation from the text
def del_punctuation(text):
    #Initiation of the variables and condition to make sure the directory "cleaned" and the file requested doesn't
    #exist already
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
    #Loop to manipulate all the character in the file and remove the punctuation
    for i in range(len(txt)):
        st = ""
        for j in range(len(txt[i])):
            #Condition to make sure the character is a letter
            if 122 >= ord(txt[i][j]) >= 97 or 255 >= ord(txt[i][j]) >= 224 or txt[i][j] == " ":
                st += txt[i][j]
            elif (txt[i][j] == "'" or txt[i][j] == "-") and j != 0:
                st += " "
            elif txt[i][j] == "\n":
                st += "\n"
        new_txt += st
    #Writing of the new file
    t.write(new_txt)
    t.close()
    os.chdir(dir)
    return ""


def del_punctuation_all_file():
    dir = os.getcwd()
    l = os.listdir(dir + "/speeches-20231105")
    for i in range(len(l)):
        #MacOS condition
        if l[i] != '.DS_Store':
            del_punctuation(l[i])
    return ""


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


#l_uni (global) list of the unique word
l_uni = tf_1()[0]

#Function to create the tf and the tf_ocu matrix
def tf_2():
    # Initiating variables
    global l_uni
    dic = tf_1()[1]
    M_tf = [["words"]]
    M_ocu = [["words"]]
    #Initiating of the first lign in M_tf/M_ocu
    for keys in dic.keys():
        M_tf[0].append(keys)
        M_ocu[0].append(keys)
    # Matrix for a term frequency in a document and the other with the tf score
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


#Function to show matrix TF, takes matrix in parameter
def show_M(M):
    global l_uni
    maxi = l_uni[0]
    for i in range(len(l_uni)):
        if len(l_uni[i]) > len(maxi):
            maxi = l_uni[i]
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="\t")
        print()
    return ""


#Function to make the idf dictionary : dic_idf = {"word": score idf}
def idf():
    # Initiating variables
    M = tf_2()[1]
    dir = os.getcwd()
    len_file = len(os.listdir(dir + "/cleaned"))
    dic_idf = {}
    #Loop to create the value to add to the dictionary
    for i in range(1,len(M)):
        cpt = 0
        for j in range(1,len(M[i])):
            if M[i][j] > 0:
                cpt += 1
        dic_idf[M[i][0]] = math.log(len_file/cpt)
    return dic_idf


#Function to create the tf_idf matrix
def tf_idf():
    # Initiating variables
    l_file = list_of_files("cleaned","txt")
    global l_uni
    dic_idf = idf()
    M_tf = tf_2()[0]
    M_tf_idf = [["words"]]
    #Initiating of the first lign in the matrix
    for i in range(len(l_file)):
        M_tf_idf[0].append(l_file[i])
    #Creation of the tf_idf matrix
    for i in range(len(l_uni)):
        l_inter = [l_uni[i]]
        for j in range(len(l_file)):
            l_inter.append(M_tf[i+1][j+1]*dic_idf[l_uni[i]])
        M_tf_idf.append(l_inter)
    return M_tf_idf
