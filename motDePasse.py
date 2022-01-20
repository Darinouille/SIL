#!usr/bin/python3

def motDePasse(login, mdp, n, p, q, r, s, t, u) :
    cpt = 0
    N = 0
    P = 0
    Q = 0
    R = 0
    nbConsec = 0
    S = 0
    accent = False

    while cpt < len(mdp) :
        if mdp[cpt] not in "0123456789" : # recompte caractères numériques consécutifs
            if nbConsec > S :
                S = nbConsec
            nbConsec = 0
            
        if mdp[cpt] in "0123456789" :   # caractères numériques / caractères numériques consécutifs
            N = N + 1
            nbConsec = nbConsec + 1

        elif ord(mdp[cpt]) in range (ord("a"),ord("z")) : # caractères minuscules
            P = P + 1

        elif mdp[cpt] in "([!\"#$%&'*+,-./;<=>?@\\^_`|}~]),{" : # caractères spéciaux
            Q = Q + 1

        elif ord(mdp[cpt]) in range (ord("A"),ord("Z")) : # caractères majuscules
            R = R + 1

        else :
            accent = True
            
        cpt = cpt + 1
        
    print (N, P, Q, R, S)

    if N < n :
        return 200

    elif P < p :
        return 210

    elif Q < q :
        return 220

    elif accent :
        return 230

    elif login in mdp :  # contient le login
        return 240

    elif R < r :
        return 250

    elif S < s :
        return 260

    elif len(mdp) < t :  # nombre de caractères
        return 280

    elif mdp in u : # identique à un ancien mot de passe
        return 300
        
    else :  # mot de passe valide
        return 0
