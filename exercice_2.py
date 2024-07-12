#2. Les Structures Répétitives (while, for)
#Exercice : Créer un programme qui affiche les 10 premiers nombres pairs en utilisant
#une boucle For . Ensuite, utiliser une boucle while pour afficher les 10 premiers nombres
#impairs.
#Exercice: Créer un programme qui va demander un nombre à l’utilisateur, va s’assurer
#que c’est bien un nombre qui a été inséré et enfin va afficher les nombres entier entre le 1
#et le nombre fourni par l’utilisateur.
#Vous utiliserez les boucles For et While.
# 1.première option :un programme qui affiche les 10 premiers nombres pairs en utilisant
#une boucle For .
print("Les 10 premiers nombres pairs:")
for i in range(2, 21, 2):
    print(i)
        #utiliser une boucle while pour afficher les 10 premiers nombres
#impairs.
print("Les 10 premiers nombres impairs:")
i = 1
count = 0
while count < 10:
    print(i)
    i += 2
    count += 
