DORIAN MAURY - ANDREA DARIO

Lien GitHub : https://github.com/Andrea01111/Projet_ChatBot_Dorian_Andrea


Dans la première partie du projet vous avez la possibilité d'accéder à un menu interactif dans le ficher "main.py" qui vous propose d'utiliser les différentes fonctions développées dans le fichier "functionality.py".

Ces fonctions vont utiliser les fonctions du développement du score tf-idf dans le fichier "functions.py" pour vous renvoyer le résultat attendu.
Plusieurs fonctions sont à votre disposition (5): 

- lower_tf_idf(), Affichage de la liste des mots les moins importants dans le corpus de documents.
- max_tf_idf(), Affichage du mot ayant le score TD-IDF le plus élevé parmi tous les discours.
- max_f_word(), Affichage du mot le plus répété par le président Chirac.
- find_word(), Affichage des noms des présidents qui ont parlé de la Nation et celui qui l’a répété le 	plus de fois.
- climate_eco(), Affichage du premier président qui a parlé du climat ou de l’écologie dans les 	différents discours.

Pour parvenir à utiliser ces fonctionnalités, nous avons créé le fichier « functions.py » dans lequel on manipule les fichiers qui composent le corpus de texte qui nous sert de base de données pour ce projet. 
Par exemple, on va isoler les noms et prénoms des différents président avec les fonctions « first_name() » et « show_president() » qui permettent de renvoyer le nom du président associé avec son prénom qu’on demande de saisir juste avant.
On supprime toute la ponctuation présente dans les différents documents à l’aide de la fonction « cleaned_file() » pour pouvoir simplifier les fonctions qui ont servi pour créer les fonctionnalités.
Nous avons également mis en place une matrice contenant les scores TF-IDF de tous les mots présents dans le corpus. Il s’agit d’un indice permettant de savoir si un mot est dit plus important qu’un autre. Ainsi, plus son score est élevé, plus le mot sera dit « important »  


Dans la seconde partie du projet, vous aurez beaucoup plus de possibilités car en plus de pouvoir accéder aux différentes fonctionnalités précédentes dans le menu « main.py », vous pourrez également poser une question ouverte à notre chatbot qui y répondra à l’aide du corpus de texte qui lui sert de base de données. Ainsi, dans le fichier « functions2.py » nous sommes passés par une succession d’étapes qui ont permis l’élaboration d’une réponse à une question ouverte. 
Tout d’abord, nous avons « Tokeniser » la question pour pouvoir séparer chaque mot qui la compose à l’aide de la fonction « token() »
Nous avons créé la fonction « word_in_corpus() » pour pouvoir rechercher si les mots que contiennent la question sont présent dans les différents textes du corpus ou non
Nous avons ensuite recherché le vecteur TF-IDF de la question pour pouvoir assimiler à chaque mot un nombre plus ou moins élevé qui permettra de lier le mot le plus important de la question à un texte. 
On a ainsi établi une similarité à l’aide de plusieurs fonctions qui permettent de la calculer puis on associe à cette question un document dans lequel on va rechercher le mot le plus important de la question qu’on a pu isoler précédemment.
Enfin, nous avons créé une fonction afin de générer la meilleure réponse possible en séparant le document par phrase. Il suffit donc de ressortir la première phrase contenant le mot rechercher pour générer une réponse. On ajoute ensuite des morceaux de phrase à la réponse qui permettent de supprimer son aspect brut à l’aide de la fonction « p_answer() »
On obtient ainsi une réponse pour chaque question posée à notre chatbot 