#Fichier d'enquete avec le Nom, Prénom, Age et Ville de résidence de l'utilisateur
#Le programme doit afficher les informations de l'utilisateur à la fin de l'enquete

#Demander le nom de l'utilisateur
nom = input("Quel est votre nom ? ")
#Demander le prénom de l'utilisateur
prenom = input("Quel est votre prénom ? ")
#Demander l'âge de l'utilisateur
age = input("Quel est votre âge ? ")
#Demander la ville de résidence de l'utilisateur
ville = input("Quelle est votre ville de résidence ? ")
#Afficher les informations de l'utilisateur
print("Voici les informations que vous avez fournies :")
print("Nom : {}".format(nom))
print("Prénom : {}".format(prenom))
print("Âge : {}".format(age))
print("Ville de résidence {}: ".format(ville))
print("Merci d'avoir participé à cette enquête !")