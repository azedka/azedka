import random

a = " "
z = " "
e = " "
r = " "
t = " "
y = " "
u = " "
i = " "
o = " "
p = " "
q = " "
s = " "
d = " "
f = " "
g = " "
h = " "
j = " "
k = " "
l = " "
m = " "
w = " "
x = " "
c = " "
v = " "
b = " "
n = " "
a1 = " "
z1 = " "
e1 = " "
r1 = " "
t1 = " "
y1 = " "
u1 = " "
i1 = " "
o1 = " "
p1 = " "
q1 = " "
s1 = " "
d1 = " "
f1 = " "
g1 = " "
h1 = " "
j1 = " "
k1 = " "
l1 = " "


def grille():
    global a, z, e, r, t, y, u, i, o, p, q, s, d, f, g, h, j, k, l, m, w, x, c, v, b, n, a1, z1, e1, r1, t1, y1, u1, i1, o1, p1, q1, s1, d1, f1, g1, h1, j1, k1, l1, m1
    print("                              -  1  -  2  -  3  -  4  -  5  -  6  -  7  -  8  -  9  -")
    print("                              | ", a, " | ", z, " | ", e, " | ", r, " | ", t, " | ", y, " | ", u, " | ", i, " | ", o, " |")
    print("                              |-----------------------------------------------------|")
    print("                              | ", p, " | ", q, " | ", s, " | ", d, " | ", f, " | ", g, " | ", h, " | ", j, " | ", k, " |")
    print("                              |-----------------------------------------------------|")
    print("                              | ", l, " | ", m, " | ", w, " | ", x, " | ", c, " | ", v, " | ", b, " | ", n, " | ", a1, " |")
    print("                              |-----------------------------------------------------|")
    print("                              | ", z1, " | ", e1, " | ", r1, " | ", t1, " | ", y1, " | ", u1, " | ", i1, " | ", o1, " | ", p1, " |")
    print("                              |-----------------------------------------------------|")
    print("                              | ", q1, " | ", s1, " | ", d1, " | ", f1, " | ", g1, " | ", h1, " | ", j1, " | ", k1, " | ", l1, " |")
    print("                              |_____________________________________________________|")


def start():
    global a, z, e, r, t, y, u, i, o, p, q, s, d, f, g, h, j, k, l, m, w, x, c, v, b, n, a1, z1, e1, r1, t1, y1, u1, i1, o1, p1, q1, s1, d1, f1, g1, h1, j1, k1, l1, m1, tour
    a = " "
    z = " "
    e = " "
    r = " "
    t = " "
    y = " "
    u = " "
    i = " "
    o = " "
    p = " "
    q = " "
    s = " "
    d = " "
    f = " "
    g = " "
    h = " "
    j = " "
    k = " "
    l = " "
    m = " "
    w = " "
    x = " "
    c = " "
    v = " "
    b = " "
    n = " "
    a1 = " "
    z1 = " "
    e1 = " "
    r1 = " "
    t1 = " "
    y1 = " "
    u1 = " "
    i1 = " "
    o1 = " "
    p1 = " "
    q1 = " "
    s1 = " "
    d1 = " "
    f1 = " "
    g1 = " "
    h1 = " "
    j1 = " "
    k1 = " "
    l1 = " "


tour = 1


def verifierX(a, z, e, r, t, y, u, i, o,
              p, q, s, d, f, g, h, j, k,
              l, m, w, x, c, v, b, n, a1,
              z1, e1, r1, t1, y1, u1, i1, o1, p1,
              q1, s1, d1, f1, g1, h1, j1, k1, l1):
    # Organiser les variables dans une grille
    grille = [[a, z, e, r, t, y, u, i, o],
              [p, q, s, d, f, g, h, j, k],
              [l, m, w, x, c, v, b, n, a1],
              [z1, e1, r1, t1, y1, u1, i1, o1, p1],
              [q1, s1, d1, f1, g1, h1, j1, k1, l1]]

    # Vérifier horizontalement
    for ligne in grille:
        for i in range(len(ligne) - 3):
            if ligne[i] == ligne[i+1] == ligne[i+2] == ligne[i+3] == "X":
                return True

    # Vérifier verticalement
    for j in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == "X":
                return True

    # Vérifier diagonalement (de gauche à droite)
    for i in range(len(grille) - 3):
        for j in range(len(grille[0]) - 3):
            if grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == "X":
                return True

    # Vérifier diagonalement (de droite à gauche)
    for i in range(len(grille) - 3):
        for j in range(3, len(grille[0])):
            if grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == "X":
                return True

    return False


def verifierO(a, z, e, r, t, y, u, i, o,
              p, q, s, d, f, g, h, j, k,
              l, m, w, x, c, v, b, n, a1,
              z1, e1, r1, t1, y1, u1, i1, o1, p1,
              q1, s1, d1, f1, g1, h1, j1, k1, l1):
    # Organiser les variables dans une grille
    grille = [[a, z, e, r, t, y, u, i, o],
              [p, q, s, d, f, g, h, j, k],
              [l, m, w, x, c, v, b, n, a1],
              [z1, e1, r1, t1, y1, u1, i1, o1, p1],
              [q1, s1, d1, f1, g1, h1, j1, k1, l1]]

    # Vérifier horizontalement
    for ligne in grille:
        for i in range(len(ligne) - 3):
            if ligne[i] == ligne[i+1] == ligne[i+2] == ligne[i+3] == "O":
                return True

    # Vérifier verticalement
    for j in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] == "O":
                return True

    # Vérifier diagonalement (de gauche à droite)
    for i in range(len(grille) - 3):
        for j in range(len(grille[0]) - 3):
            if grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] == "O":
                return True

    # Vérifier diagonalement (de droite à gauche)
    for i in range(len(grille) - 3):
        for j in range(3, len(grille[0])):
            if grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3] == "O":
                return True

    return False


def tourX():
    print("                   TOUR DU JOUEUR 1 (X)")
    global a, z, e, r, t, y, u, i, o, p, q, s, d, f, g, h, j, k, l, m, w, x, c, v, b, n, a1, z1, e1, r1, t1, y1, u1, i1, o1, p1, q1, s1, d1, f1, g1, h1, j1, k1, l1, m1, tour
    print("                    Tours = ", tour)
    choix = int(input("                    Rentrez la colonne ou vous voulez placer votre pion : "))
    if choix == 1:
        if q1 == " ":
                q1 = "X"
                grille()
        elif z1 == " ":
                z1 = "X"
                grille()
        elif l == " ":
                l = "X"
                grille()
        elif p == " ":
                p = "X"
                grille()
        elif a == " ":
                a = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 2:
        if s1 == " ":
                s1 = "X"
                grille()
        elif e1 == " ":
                e1 = "X"
                grille()
        elif m == " ":
                m = "X"
                grille()
        elif q == " ":
                q = "X"
                grille()
        elif z == " ":
                z = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 3:
        if d1 == " ":
                d1 = "X"
                grille()
        elif r1 == " ":
                r1 = "X"
                grille()
        elif w == " ":
                w = "X"
                grille()
        elif s == " ":
                s = "X"
                grille()
        elif e == " ":
                e = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 4:
        if f1 == " ":
                f1 = "X"
                grille()
        elif t1 == " ":
                t1 = "X"
                grille()
        elif x == " ":
                x = "X"
                grille()
        elif d == " ":
                d = "X"
                grille()
        elif r == " ":
                r = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 5:
        if g1 == " ":
                g1 = "X"
                grille()
        elif y1 == " ":
                y1 = "X"
                grille()
        elif c == " ":
                c = "X"
                grille()
        elif f == " ":
                f = "X"
                grille()
        elif t == " ":
                t = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 6:
        if h1 == " ":
                h1 = "X"
                grille()
        elif u1 == " ":
                u1 = "X"
                grille()
        elif v == " ":
                v = "X"
                grille()
        elif g == " ":
                g = "X"
                grille()
        elif y == " ":
                y = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 7:
        if j1 == " ":
                j1 = "X"
                grille()
        elif i1 == " ":
                i1 = "X"
                grille()
        elif b == " ":
                b = "X"
                grille()
        elif h == " ":
                h = "X"
                grille()
        elif u == " ":
                u = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 8:
        if k1 == " ":
                k1 = "X"
                grille()
        elif o1 == " ":
                o1 = "X"
                grille()
        elif n == " ":
                n = "X"
                grille()
        elif j == " ":
                j = "X"
                grille()
        elif i == " ":
                i = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    if choix == 9:
        if l1 == " ":
                l1 = "X"
                grille()
        elif p1 == " ":
                p1 = "X"
                grille()
        elif a1 == " ":
                a1 = "X"
                grille()
        elif k == " ":
                k = "X"
                grille()
        elif o == " ":
                o = "X"
                grille()
        else:
            print("Case deja occupé")
            tourX()
    tour += 1

def tourO():
    print("                   TOUR DU JOUEUR 2 (O)")
    global a, z, e, r, t, y, u, i, o, p, q, s, d, f, g, h, j, k, l, m, w, x, c, v, b, n, a1, z1, e1, r1, t1, y1, u1, i1, o1, p1, q1, s1, d1, f1, g1, h1, j1, k1, l1, m1, tour
    print("                    Tours = ", tour)
    choix = int(input("                    Rentrez la colonne ou vous voulez placer votre pion : "))
    if choix == 1:
        if q1 == " ":
                q1 = "O"
                grille()
        elif z1 == " ":
                z1 = "O"
                grille()
        elif l == " ":
                l = "O"
                grille()
        elif p == " ":
                p = "O"
                grille()
        elif a == " ":
                a = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 2:
        if s1 == " ":
                s1 = "O"
                grille()
        elif e1 == " ":
                e1 = "O"
                grille()
        elif m == " ":
                m = "O"
                grille()
        elif q == " ":
                q = "O"
                grille()
        elif z == " ":
                z = ""
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 3:
        if d1 == " ":
                d1 = "O"
                grille()
        elif r1 == " ":
                r1 = "O"
                grille()
        elif w == " ":
                w = "O"
                grille()
        elif s == " ":
                s = "O"
                grille()
        elif e == " ":
                e = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 4:
        if f1 == " ":
                f1 = "O"
                grille()
        elif t1 == " ":
                t1 = "O"
                grille()
        elif x == " ":
                x = "O"
                grille()
        elif d == " ":
                d = "O"
                grille()
        elif r == " ":
                r = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 5:
        if g1 == " ":
                g1 = "O"
                grille()
        elif y1 == " ":
                y1 = "O"
                grille()
        elif c == " ":
                c = "O"
                grille()
        elif f == " ":
                f = "O"
                grille()
        elif t == " ":
                t = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 6:
        if h1 == " ":
                h1 = "O"
                grille()
        elif u1 == " ":
                u1 = "O"
                grille()
        elif v == " ":
                v = "O"
                grille()
        elif g == " ":
                g = "O"
                grille()
        elif y == " ":
                y = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 7:
        if j1 == " ":
                j1 = "O"
                grille()
        elif i1 == " ":
                i1 = "O"
                grille()
        elif b == " ":
                b = "O"
                grille()
        elif h == " ":
                h = "O"
                grille()
        elif u == " ":
                u = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 8:
        if k1 == " ":
                k1 = "O"
                grille()
        elif o1 == " ":
                o1 = "O"
                grille()
        elif n == " ":
                n = "O"
                grille()
        elif j == " ":
                j = "O"
                grille()
        elif i == " ":
                i = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    if choix == 9:
        if l1 == " ":
                l1 = "O"
                grille()
        elif p1 == " ":
                p1 = "O"
                grille()
        elif a1 == " ":
                a1 = "O"
                grille()
        elif k == " ":
                k = "O"
                grille()
        elif o == " ":
                o = "O"
                grille()
        else:
            print("Case deja occupé")
            tourO()
    tour += 1

def tourpc():
    print("                   TOUR DU PC (O)")
    global a, z, e, r, t, y, u, i, o, p, q, s, d, f, g, h, j, k, l, m, w, x, c, v, b, n, a1, z1, e1, r1, t1, y1, u1, i1, o1, p1, q1, s1, d1, f1, g1, h1, j1, k1, l1, m1, tour
    print("                    Tours = ", tour)
    choix = random.randint(1, 9)
    if choix == 1:
        if q1 == " ":
            q1 = "O"
            grille()
        elif z1 == " ":
            z1 = "O"
            grille()
        elif l == " ":
            l = "O"
            grille()
        elif p == " ":
            p = "O"
            grille()
        elif a == " ":
            a = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 2:
        if s1 == " ":
            s1 = "O"
            grille()
        elif e1 == " ":
            e1 = "O"
            grille()
        elif m == " ":
            m = "O"
            grille()
        elif q == " ":
            q = "O"
            grille()
        elif z == " ":
            z = ""
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 3:
        if d1 == " ":
            d1 = "O"
            grille()
        elif r1 == " ":
            r1 = "O"
            grille()
        elif w == " ":
            w = "O"
            grille()
        elif s == " ":
            s = "O"
            grille()
        elif e == " ":
            e = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 4:
        if f1 == " ":
            f1 = "O"
            grille()
        elif t1 == " ":
            t1 = "O"
            grille()
        elif x == " ":
            x = "O"
            grille()
        elif d == " ":
            d = "O"
            grille()
        elif r == " ":
            r = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 5:
        if g1 == " ":
            g1 = "O"
            grille()
        elif y1 == " ":
            y1 = "O"
            grille()
        elif c == " ":
            c = "O"
            grille()
        elif f == " ":
            f = "O"
            grille()
        elif t == " ":
            t = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 6:
        if h1 == " ":
            h1 = "O"
            grille()
        elif u1 == " ":
            u1 = "O"
            grille()
        elif v == " ":
            v = "O"
            grille()
        elif g == " ":
            g = "O"
            grille()
        elif y == " ":
            y = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 7:
        if j1 == " ":
            j1 = "O"
            grille()
        elif i1 == " ":
            i1 = "O"
            grille()
        elif b == " ":
            b = "O"
            grille()
        elif h == " ":
            h = "O"
            grille()
        elif u == " ":
            u = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 8:
        if k1 == " ":
            k1 = "O"
            grille()
        elif o1 == " ":
            o1 = "O"
            grille()
        elif n == " ":
            n = "O"
            grille()
        elif j == " ":
            j = "O"
            grille()
        elif i == " ":
            i = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    if choix == 9:
        if l1 == " ":
            l1 = "O"
            grille()
        elif p1 == " ":
            p1 = "O"
            grille()
        elif a1 == " ":
            a1 = "O"
            grille()
        elif k == " ":
            k = "O"
            grille()
        elif o == " ":
            o = "O"
            grille()
        else:
            print("Case deja occupé")
            tourpc()
    tour += 1




def playnormal():
    while True:
        tourX()
        if verifierX(a, z, e, r, t, y, u, i, o,
                     p, q, s, d, f, g, h, j, k,
                     l, m, w, x, c, v, b, n, a1,
                     z1, e1, r1, t1, y1, u1, i1, o1, p1,
                     q1, s1, d1, f1, g1, h1, j1, k1, l1):
            print("                    Joueur 1 a gagné(X)")
            break
        tourO()
        if verifierO(a, z, e, r, t, y, u, i, o,
                     p, q, s, d, f, g, h, j, k,
                     l, m, w, x, c, v, b, n, a1,
                     z1, e1, r1, t1, y1, u1, i1, o1, p1,
                     q1, s1, d1, f1, g1, h1, j1, k1, l1):
            print("                    Joueur 2 a gagné(O)")
            break

def playpc():
    while True:
        tourX()
        if verifierX(a, z, e, r, t, y, u, i, o,
                     p, q, s, d, f, g, h, j, k,
                     l, m, w, x, c, v, b, n, a1,
                     z1, e1, r1, t1, y1, u1, i1, o1, p1,
                     q1, s1, d1, f1, g1, h1, j1, k1, l1):
            print("                    Joueur 1 a gagné(X)")
            break
        tourpc()
        if verifierO(a, z, e, r, t, y, u, i, o,
                     p, q, s, d, f, g, h, j, k,
                     l, m, w, x, c, v, b, n, a1,
                     z1, e1, r1, t1, y1, u1, i1, o1, p1,
                     q1, s1, d1, f1, g1, h1, j1, k1, l1):
            print("                    l ordianteur a gagné(O)")
            break

def jeu_pc():
    global tour
    while True:
        tour = 0
        start()
        playpc()
        stop = input("          Voulez vous recommencer ?(oui ou non) : ")
        if stop == "non":
            print("          Au revoir")
            break

def jeu_nrml():
    global tour
    while True:
        tour = 0
        start()
        playnormal()
        stop = input("                    Voulez vous recommencer ?(oui ou non) : ")
        if stop == "non":
            print("          Au revoir")
            break


while True:
    dm = int(input("-_-_-_--_-_-_-_-_-_-_-__---___--_-_-_Voulez vous jouer en 1v1 ou contre l'ordinateur (1/2): "))
    if dm == 1:
        jeu_nrml()
    else:
        jeu_pc()
