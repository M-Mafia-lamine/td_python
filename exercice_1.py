#exercice N°1
#    a. "Excellent" pour les notes de 18 et plus
#b. "Très bien" pour les notes entre 16 et 18
#c. "Bien" pour les notes entre 14 et 16
#d. "Satisfaisant" pour les notes entre 12 et 14
#e. “Passable” pour les notes entre 10 et 12
#f. "Échec" pour les notes inférieures à 10
note = input("quelle est votre note ")
if note.isdecimal():
    print("c'est un digit")
        
    if int(note) >= 18:
        print("excellent")
    elif int(note) >= 16 and int(note) < 18 :
        print("très bien")
    elif int(note) >= 14 and int(note) < 16 :
        print("bien")
    elif int(note) >= 12 and int(note) < 14 :
        print("satisfaisant")
    elif int(note) >= 10 and int(note) < 12 :
        print("passable")
    elif int(note) < 10                     :
        print("échec")
else: 
    print("ce n'est pas un digit")
