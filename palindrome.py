## KWJE ##

def palindrome(chaine):

    l = list(chaine)  # ici jai converti le string chaine en list l.  Je pouvais le faire directement comme d'habitude avec la syntaxe de convertion qu'on utilisait d'habitude
                      ## cette syntaxe:  chaine = list(input("")) ici l'utilisateur entre directement un mot qui va se diviser en liste


    i = len(l) - 1  ## pour cette boucle comme je veux lire le tableau a l'envers, j'initialise le i a la derniere valeur ou dernier element du tableau
                    ## la au lieu d'incrementer je decremente de 1


    l_reverse = []

    while i >= 0:
        k = l[i]
        l_reverse.append(k)   ## ici a chaque fois que k prens l'element du tableau à l'envers je le met dans une autre liste l_reverse
        i = i - 1

        lop = str(l_reverse)  ## ici je reconverti le tableau h qui contient les lettres à l'envers en un string


    v = bool()
    if l == l_reverse:
        v = True
    else:
        v = False

    return v



m = input("Donner un mot ")

t_or_f = palindrome(m)

print(t_or_f)

if t_or_f == True:
    print(m, "est un palindrome")
else:
    print(m, "n'est pas un palindrome")




