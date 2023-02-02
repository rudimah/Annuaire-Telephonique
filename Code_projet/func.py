import csv

def lecture_csv(fichier, delimiteur):
    """
    Paramètre : un chemin vers un fichier CSV
    Valeur renvoyée : un tableau de dictionnaires, extraction de la table contenue dans le fichier
    """
    f = open(fichier, mode = 'r', encoding = 'utf8', newline='')
    reader = csv.DictReader(f, delimiter = delimiteur)  #création de l'objet reader
    table = [dict(enregistrement) for enregistrement in reader]
    f.close()
    return table

def ecriture_csv(table, fichier, delimiteur):
    """
    Paramètre : 
        un chemin vers un fichier CSV
        une table comme tableau de dictionnaires partageant les mêmes clefs, de valeurs str
    Valeur renvoyée :
        None, écrit table dans fichier avec Dictriter du  module CSV 
    """
    g = open(fichier, mode = 'w', encoding = 'utf8', newline='')
    attributs = list(table[0].keys())
    writer = csv.DictWriter(g, delimiter = delimiteur, fieldnames = attributs) #création de l'objet writer
    writer.writeheader()   #écriture des attibuts
    for enregistrement in table:
        writer.writerow(enregistrement)  #écriture des enregistrements
    g.close()
    
def tri(lst):
    return lst['nom']

def vcard(fichier, lst):
    """crée un ficher vcf avec les informations de l'utilisateur """
    fichier = open(fichier,'w') 
    fichier.write('BEGIN:VCARD\n')
    fichier.write('VERSION:2.1\n')
    fichier.write('FN:'+lst[0]['nom']+'\n')
    fichier.write('TEL;CELL:'+lst[0]['numéro']+'\n')
    fichier.write('Email:'+lst[0]['adresse_mail']+'\n')
    fichier.write('ADR;TYPE=dom:;;'+lst[0]['adresse_postale']+';;\n')
    fichier.write('END:VCARD\n')
    fichier.close() 