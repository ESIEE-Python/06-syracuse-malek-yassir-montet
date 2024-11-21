"""Module pour afficher la suite de Syracluse"""
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Fonction qui affiche créé l'affichage du graphe"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """Fonction qui calcule et renvoie la liste de Syracuse d'un nombre n"""
    l = [n]
    while l[-1] > 1:
        if l[-1] % 2 == 0:
            l.append(l[-1] // 2)
        else:
            l.append(3 * l[-1] + 1)
    return l

def temps_de_vol(l):
    """Fonction qui renvoie le temps de vol d'une liste de Syracuse"""
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """Fonction qui renvoie le temps de vol en altitude d'une liste de Syracuse"""
    n = 0
    for i in l:
        if i < l[0]:
            return n-1
        n += 1
    return n-1

def altitude_maximale(l):
    """Fonction qui renvoie l'altidude maximale atteinte par une liste de Syracuse"""
    n = l[0]
    for i in l:
        n = max(n, i)
    return n


#### Fonction principale


def main():
    """Fonction main qui affiche les valeurs d'une suite de Syracuse"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
