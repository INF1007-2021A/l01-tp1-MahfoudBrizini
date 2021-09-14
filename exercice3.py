def decomposer(secondes):
    SECONDES_DANS_ANNEE = 60 * 60 * 24 * 365
    SECONDES_DANS_SEMAINES = 60 * 60 * 24 * 7
    SECONDES_DANS_JOUR = 60 * 60 * 24
    SECONDES_DANS_HEURE = 60 * 60
    SECONDES_DANS_MINUTES = 60

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes // SECONDES_DANS_ANNEE
    secondes -= annees * SECONDES_DANS_ANNEE

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes // SECONDES_DANS_SEMAINES
    secondes -= semaines * SECONDES_DANS_SEMAINES

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes // SECONDES_DANS_JOUR
    secondes -= jours * SECONDES_DANS_JOUR

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes // SECONDES_DANS_HEURE
    secondes -= heures * SECONDES_DANS_HEURE

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = secondes // SECONDES_DANS_MINUTES
    secondes -= minutes * SECONDES_DANS_MINUTES

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees, semaines, jours, heures, minutes, secondes)

    return (annees, semaines, jours, heures, minutes, secondes)


if __name__ == "__main__":
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
