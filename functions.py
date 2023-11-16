import os
import time

print()

def makedir(txt):
    os.mkdir(txt)
    print(f"Making of the directory '{txt}'... ")
    time.sleep(1)
    return ""
#zlidkn


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Call of the function
directory = 'speeches-20231105'
files_names = list_of_files(directory, "txt")
#print_list(files_names)
print(files_names)
#print()

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
print(l_name_president)

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
    if "cleaned" not in os.listdir(dir):           #Création du dossier 'cleaned' s'il n'existe pas
        makedir("cleaned")
    if text in os.listdir(dir + "/cleaned"):               #Vérification si le fichier existe déja dans 'cleaned'
        return f"The file '{text}' already exist in 'cleaned'"
    else:                                               #Changement des majuscules en minuscules
        os.chdir(dir + "/speeches-20231105")
        with open(text,"r") as t:
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
    with open(text,"w") as c:
        c.write(new_txt)
    os.chdir(dir)
    return ""


#print(cleaned_file("Nomination_Macron.txt"))


def del_punctuation(text):
    dir = os.getcwd()
    if "cleaned" not in os.listdir(dir):
        cleaned_file(text)
    elif text not in os.listdir("cleaned"):
        cleaned_file(text)
    os.chdir(dir + "/cleaned")
    t = open(text,"r")
    txt = t.readlines()
    t.close()
    t = open(text,"w")
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

#print(del_punctuation("Nomination_Giscard dEstaing.txt"))

def del_punctuation_all_file():
    dir = os.getcwd()
    l = os.listdir(dir + "/speeches-20231105")
    for i in range(len(l)):
        del_punctuation(l[i])
    return ""

#print(del_punctuation_all_file())
#hfeiz
