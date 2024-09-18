#EXO 1
#def inverser_chaine(chaine):
    #chaine_inversee = ''
    #for i in range(len(chaine) - 1, -1, -1):
       #chaine_inversee += chaine[i]
   #return chaine_inversee

#print(inverser_chaine("Bonjour")) # Affiche "ruojnoB"



#EXO 2
#Créer un algorithme qui calcule la somme des éléments d'une liste.
#Exemple :
#Entrée : [1, 2, 3, 4]
#Sortie : 10
# def somme_liste(liste):
#     somme = 0
#     for i in liste:
#         somme += i
#     return somme 

# print(somme_liste([1, 2, 3, 4]))




#EXO 3
#Exercice 3 : Recherche du Plus Grand Nombre
#Écrire un script qui trouve le plus grand nombre dans une liste.
#Exemple :
#Entrée : [3, 58, 11, 21]
#Sortie : 58
# def plus_grand_nombre(liste):
#     max_nombre = liste[0]
#     for nombre in liste:
#         if nombre > max_nombre:
#             max_nombre = nombre
#     return max_nombre

# print(plus_grand_nombre([3, 58, 11, 21]))



# Exercice 4 : Calcul de la Factorielle
# Développer une fonction qui calcule la factorielle d'un nombre.
# Exemple :
# Entrée : 5
# Sortie : 120 (car 5! = 5 x 4 x 3 x 2 x 1)

# def factorielle(n):
#     produit = 0
#     i = 1
#     for k in range(1, n):
#         if i <= n:
#             produit = n*(n)
#     return produit

# print(factorielle(5))
# exercice non fini



# Exercice 5 : vérificationde palindrome
# Créer un programme qui vérifie si un mot est un palindrome (se lit de la même manière dans les deux sens).
# Exemple :
# Entrée : "radar"
# Sortie : True

def est_palindrome(mot):
    longueur = len(mot)
    for i in range ():
        if mot[i] != mot[]:
            return False
    return True

print(est_palindrome("radar"))
