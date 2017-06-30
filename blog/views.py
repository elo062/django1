# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Par défaut, Django a généré gentiment ce fichier :
from django.shortcuts import render
# Nous importons la classe HttpResponse du module django.http. Cette classe permet de retourner une réponse (texte brut, JSON ou HTML comme ici) depuis une chaîne de caractères :
from django.http import HttpResponse
from datetime import datetime



# Ajout de la fonction view_article

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_article)
    )


# Une fonction home, avec comme argument une instance de HttpRequest, nommé par convention request. Celui-ci contient des infos sur la méthode de la requête (GET, POST), les données des formulaires, la session du client, etc.
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""

# Finalement, la fonction déclare une chaîne de caractères nommée text et crée une nouvelle instance de HttpResponse à partir de cette chaîne, que la fonction renvoie ensuite au framework.
    return HttpResponse(text)

# Par la suite, ne renvoyez jamais du code HTML directement depuis la vue comme nous le faisons ici. Passez toujours par des templates. Il s'agit de respecter l'architecture du framework dont nous avons parlé dans la partie précédente afin de bénéficier de ses avantages (la structuration du code notamment).


# une vue qui renvoie juste la date actuelle à l'utilisateur :

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})



def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())


# La fonction render est une méthode qui génère un objet HttpResponse après avoir traité notre template.
# La fonction locals() va retourner un dictionnaire contenant toutes les variables locales de la fonction depuis laquelle locals() a été appelée. Les clés seront les noms de variables et les valeurs du dictionnaire seront les valeurs des variables de la fonction ! Ainsi, si nombre1 valait 42, la valeur nombre1 du dictionnaire vaudra elle aussi 42.
