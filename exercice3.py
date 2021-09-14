
def decomposer(secondes):
    secondes_dans_annes = 365 * 24 * 2600
    secondes_dans_semaine = 7 * 24 * 3600
    secondes_dans_jour = 24 * 60 * 60
    secondes_dans_heure = 60 * 60
    seconde_dans_minute = 60

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes // secondes_dans_annes
    secondes -= annees * secondes_dans_annes
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes // secondes_dans_semaine
    secondes -= semaines * secondes_dans_semaine

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes // secondes_dans_jour
    secondes -= jours * secondes_dans_jour

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes // secondes_dans_heure
    secondes -= heures * secondes_dans_heure

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = secondes // seconde_dans_minute

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes -= minutes * seconde_dans_minute

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
