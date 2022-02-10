#!/usr/bin/env python
# coding: utf-8

# In[1]:


def init_play():
    """Retourne un plateau correspondant à une nouvelle partie."""
    dico={
        "n" : 4,
        "nb_cases_libres" : 16,
        "tiles" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    return dico
    
p=init_play()
print(p)


# In[2]:


def check_indice(plateau, indice):
    """Retourne True si indice correpond à un indice valide de case pour le plateau(entre 0 et n-1)"""
    if indice>=0 and indice<=plateau["n"]-1:
        return True
    else:
        return False

p=init_play()
print(check_indice(p, 0))
print(check_indice(p, 10))
print(check_indice(p, 3))
print(check_indice(p, 4))
print(check_indice(p, -1))


# In[3]:


def check_room(plateau, lig, col):
    """Retourne True si (lig, col) est une case du plateau avec lig, col 2indices valides"""
    if check_indice(p,lig)==True and check_indice(p,col)==True:
        return True
    else:
        return False
    
p=init_play()
print(check_room(p, 2, 1))
print(check_room(p, 10, 2))
print(check_room(p, -1, 3))
print(check_room(p, 3, 3))


# In[5]:


def get_value(plateau, lig, col):
    """Retourne la valeur de la case (lig,col) et retourne une erreur si (lig,col) n'est pas valide"""
    if check_room(plateau, lig, col)==False:
        return "erreur la case n'est pas valide"
    else:
        case=lig*plateau["n"]+col
        val=plateau["tiles"][case]
        return val
    
p=init_play()
print(get_value(p, 0, 0))
print(get_value(p, 2, 3))
print(get_value(p, 1, 3))
print(get_value(p, 3, 0))
print(get_value(p, 18, 3))


# In[8]:


def set_value(plateau, lig, col, val):
    """Affecte la valeur val à la case situé aux coord. (lig, col)"""
    if check_room(plateau, lig, col)==False:
        return "erreur la case n'est pas valide"
    else:
        case=lig*plateau["n"]+col
        plateau["tiles"][case]=val
        return p["tiles"]
        
p=init_play()
print(set_value(p, 0, 0, 1))
print(set_value(p, 1, 2, 0))
print(set_value(p, 18, 3, 1))
print(set_value(p, 2, 3, 6))


# In[9]:


def is_room_empty(plateau, i, j):
    """Teste si une case est valide et retourne True si elle est libre ou sinon False"""
    if check_room(plateau, i, j)==False:
        return "erreur la case n'est pas valide"
    elif plateau["tiles"][i*plateau["n"]+j]!=0:
        return False
    else:
        return True
    
p=init_play()
print(is_room_empty(p, 0, 1))
print(is_room_empty(p, 3, 2))
print(is_room_empty(p, 15, 2))    


# In[14]:


def get_nb_empty_rooms(plateau):
    """Met à jour le nombre de cases libres du plateau actuel"""
    case_libres=0
    lig=0
    while lig<plateau["n"]:
        col=0
        while col<plateau["n"]:
            if get_value(plateau, lig, col)==0:
                case_libres+=1
            col+=1
        lig+=1
    plateau["nb_cases_libres"]=case_libres
    return plateau["nb_cases_libres"]

p=init_play()
print(p)
print(get_nb_empty_rooms(p))


# In[27]:


def is_game_over(plateau):
    """Retourne True si la partie est terminée, False sinon"""
    newp = get_nb_empty_rooms(plateau)
    if newp==0:
        return True
    else:
        return False
   
    
p1={
        "n" : 4,
        "nb_cases_libres" : 16,
        "tiles" : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]
    }
print(is_game_over(p1))
p2={
        "n" : 4,
        "nb_cases_libres" : 6,
        "tiles" : [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]
    }
print(is_game_over(p2))


# In[29]:


def get_score(plateau):
    """Retourne le score et donc le nombre de point total du plateau"""
    score=0
    i=0
    taille=plateau["n"]*plateau["n"]
    while i<taille:
        score+=plateau["tiles"][i]
        i+=1
    return score

p2={
        "n" : 4,
        "nb_cases_libres" : 6,
        "tiles" : [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]
}
print(get_score(p2))


# In[30]:


def simple_display(plateau):
    """Affichage du plateau simplifié"""
    esp="  "
    i=0
    y=0
    taillef=plateau["n"]
    while i<plateau["n"]:
        lig=""
        while y<taillef and taillef<=plateau["n"]**2:
            lig+= str(plateau["tiles"][y]) + esp
            y+=1
        print(lig)
        taillef+=plateau["n"]
        i+=1


p=init_play()
p1={
        "n" : 4,
        "nb_cases_libres" : 16,
        "tiles" : [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]
    }
print(p1["tiles"])
print()
simple_display(p1)


# In[31]:


def medium_display(plateau):
    """Affichage du plateau avec délimitations textuelles des cases"""
    esp="  "
    sep="* "
    print(22*"*")
    taillef=plateau["n"]
    y=0
    i=0
    while i<plateau["n"]:
        lig="*  "
        while y<taillef and taillef<=plateau["n"]**2:
            lig+= str(plateau["tiles"][y]) + esp + sep
            y+=1
        print(lig)
        print(22*"*")
        taillef+=plateau["n"]
        i+=1
    
print(p1["tiles"])
print()
medium_display(p1)


# In[32]:


from random import*
def get_next_alea_tiles(plateau, mode):
    if mode != "init" and mode != "encours":#vérifie que le mode est valide
        return "Le mode saisie n'est pas valide"
    
    if is_game_over(p)==False:#vérifie si la partie est terminé ou non
        end=True
    else:
        end=False
    
    if mode =="init":#mode init retourne un dico qui contient 2 tuiles
        dico_mode={"mode":"init",
                   0 : {"val": 1,
                               "lig": randint(0, p["n"]-1),
                               "col": randint(0, p["n"]-1)},
                   1 : {"val": 2,
                               "lig": randint(0, p["n"]-1),
                               "col": randint(0, p["n"]-1)},
                   "check" : end
                  }
        return dico_mode
    
    lig=randint(0, p["n"]-1)
    col=randint(0, p["n"]-1)
    val=randint(1, 3)
    if mode == "encours" and is_room_empty(plateau, lig, col)==True:#mode encours retourne un dico à 1 tuile
        dico_mode={"mode":"encours",
                   0 : {"val": val,
                               "lig": lig,
                               "col": col},
                   "check" : end
                  }
    return dico_mode
    

p=init_play()
print(get_next_alea_tiles(p, "init"))
print(get_next_alea_tiles(p, "encours"))


# In[33]:


def put_next_tiles(plateau, tiles):
    """p=plateau t=dico_de_get_next_alea_tiles place 1/2 tuiles dans le plateau en fonction du mode choisi"""
    val0=tiles[0]["val"]
    lig0=tiles[0]["lig"]
    col0=tiles[0]["col"]
    if is_room_empty(plateau, lig0, col0)==True:
        set_value(plateau, lig0, col0, val0)
    if tiles["mode"]=="init":
        val1=tiles[1]["val"]
        lig1=tiles[1]["lig"]
        col1=tiles[1]["col"]
    if tiles["mode"]=="init" and is_room_empty(plateau, lig1, col1)==True:
        set_value(plateau, lig1, col1, val1)
    return plateau
    
p1=init_play()
t1=get_next_alea_tiles(p1, "init")
newp1=put_next_tiles(p1, t1)
print(t1)
print(newp1)
simple_display(newp1)

print()
p2=init_play()
t2=get_next_alea_tiles(p2, "encours")
newp2=put_next_tiles(p2, t2)
print(t2)
print(newp2)
simple_display(p2)


# In[34]:


def line_pack(plateau, num_lig, debut, sens):
    y=num_lig*plateau["n"]+debut
    j=debut
    if sens==1:
        while j<plateau["n"]-1:
            plateau["tiles"][y]=plateau["tiles"][y+1]
            y+=1
            j+=1
    else:
        while j>0:
            plateau["tiles"][y]=plateau["tiles"][y-1]
            y-=1
            j-=1
    plateau["tiles"][y]=0
    return plateau


pline={
    "n" : 4,
    "nombres_cases_libres" : 6,
    "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
}
simple_display(pline)
print()
newpline=line_pack(pline, 1, 0, 1)
simple_display(newpline)
print()
newpline=line_pack(pline, 1, 2, 1)
simple_display(newpline)
print()
newpline=line_pack(pline, 1, 3, 0)
simple_display(newpline)
print()
newpline=line_pack(pline, 1, 2, 0)
simple_display(newpline)


# In[35]:


def column_pack(plateau, num_col, debut, sens):
    y=plateau["n"]*debut+num_col
    j=debut
    if sens==1:
        while j<plateau["n"]-1:
            plateau["tiles"][y]=plateau["tiles"][y+plateau["n"]]
            y+=plateau["n"]
            j+=1
    else:
        while j>0:
            plateau["tiles"][y]=plateau["tiles"][y-plateau["n"]]
            y-=plateau["n"]
            j-=1
    plateau["tiles"][y]=0
    return plateau


pline={
    "n" : 4,
    "nombres_cases_libres" : 6,
    "tiles" : [0, 2, 0, 0, 0, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0]
}
simple_display(pline)
print()
dico=column_pack(pline, 1, 2, 1)
simple_display(dico)
print()
dico=column_pack(pline, 1, 1, 0)
simple_display(dico)


# In[36]:


def line_move(plateau, num_lig, sens):
    y=num_lig*plateau["n"]
    if plateau["tiles"][y]!=0:
        return plateau
    elif sens==1:
        line_pack(plateau, num_lig, 0,sens)
        fin=y+plateau["n"]-1
        while y<fin:
            if plateau["tiles"][y]==plateau["tiles"][y+1]:
                plateau["tiles"][y]=plateau["tiles"][y]*2
                plateau["tiles"][y+1]=0
            y+=1
    else:
        line_pack(plateau, num_lig, plateau["n"], sens)
        while y>0:
            if plateau["tiles"][y]==plateau["tiles"][y-1]:
                plateau["tiles"][y]=plateau["tiles"][y]*2
                plateau["tiles"][y-1]=0
            y-=1
    return plateau
      
    
p={
    "n" : 4,
    "nombres_cases_libres" : 6,
    "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
}   
simple_display(p)
print()
p=line_move(p, 1, 1)
simple_display(p)
print()
p=line_move(p, 1, 1)
simple_display(p)
print()
p=line_move(p, 1, 0)
simple_display(p)


# In[37]:


def column_move(plateau, num_lig, sens):
    y=num_lig*plateau["n"]
    if plateau["tiles"][y]!=0:
        return plateau
    elif sens==1:
        line_pack(plateau, num_lig, 0,sens)
    else:
        line_pack(plateau, num_lig, plateau["n"], sens)
    fin=y+plateau["n"]-1
    while y<fin:
        if plateau["tiles"][y]==plateau["tiles"][y+1]:
            plateau["tiles"][y]=plateau["tiles"][y]*2
            plateau["tiles"][y+1]=0
        y+=1
    return plateau
      
    
p={
    "n" : 4,
    "nombres_cases_libres" : 6,
    "tiles" : [0, 2, 0, 0, 0, 2, 3, 3, 0, 2, 2, 0, 0, 0, 0, 0]
}   
simple_display(p)
print()
p=column_move(p, 1, 1)
simple_display(p)
print()
p=column_move(p, 1, 1)
simple_display(p)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




