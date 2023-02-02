import os
from func import lecture_csv, ecriture_csv, tri, vcard
from flask import Flask, render_template, request, redirect

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Flask est un micro framework open-source de developpement
# web en Python
# creation de l'application web
app = Flask('contact', template_folder=template_dir)
liste_des_contact = [{'nom': 'Regan',
  'numéro': '0897329323',
  'adresse_postale': 'csc',
  'adresse_mail': 'regan@email.fr'},
                     {'nom': 'Hamidur','numéro': '0897329323',
                      'adresse_postale': 'csc','adresse_mail': 'regan@email.fr'}]
contact_selectionner = []
contact_rechercher = []
contact_modifier = []
contact_a_modifier = []
nvx_lst= []
contact_a_partager=[]


@app.route('/contact.html')
def contact():
    contact_a_modifier.clear()
    contact_selectionner.clear()
    ecriture_csv(liste_des_contact, "liste_des_contactes.csv", ";")
    lecture_csv("liste_des_contactes.csv", ";")
    return render_template('contact.html', Contactes=liste_des_contact, )



@app.route('/search-contact.html')
def search_contact():
    return render_template('search-contact.html', contact_recherche = contact_rechercher)

@app.route('/search', methods=['POST'])
def rechercher():
    search_input = request.form.get('contactsearch')
    for i in range(len(liste_des_contact)):
        dico = liste_des_contact[i]
        if dico['nom'] == search_input:
            contact_rechercher.append(dico)
    return redirect('search-contact.html')


@app.route('/modifier-contact.html')
def modifier_contact():
    return render_template('modifier-contact.html', Contactes = contact_a_modifier)

@app.route('/modifier', methods=['POST'])
def modif_lien():
    contact_selectionner.append(int(request.form.get("compteur")))
    if request.form.get("modifier"):
        contact_a_modifier.append(liste_des_contact[int(request.form.get("compteur"))])
        return redirect('/modifier-contact.html')

@app.route('/modif', methods=['POST'])
def modif_contact():
    dico = {}
        
    dico['nom'] = request.form['Nom']
    dico['numéro'] = request.form['Numéro']
    dico['adresse_postale'] = request.form['Adresse']
    dico['adresse_mail'] = request.form['Mail']
    liste_des_contact[contact_selectionner[0]] = dico
    ecriture_csv(liste_des_contact, "liste_des_contactes.csv", ";")
    lecture_csv("liste_des_contactes.csv", ";")
    return redirect('/contact.html')
        

@app.route('/info', methods=['POST'])
def nvx_contact():
    nv_contact = {}
    nom =  request.form['Nom']
    nv_contact['nom'] = nom.title()
    nv_contact['numéro'] = request.form['Numéro']
    nv_contact['adresse_postale'] = request.form['Adresse']
    nv_contact['adresse_mail'] = request.form['Mail']
    liste_des_contact.append(nv_contact)
    ecriture_csv(liste_des_contact, "liste_des_contactes.csv", ";")
    lecture_csv("liste_des_contactes.csv", ";")

    return redirect('/contact.html')

@app.route('/supp', methods=['POST'])
def supprimer_contact():
    """Si un utilisateur appuie sur le bouton supprimer, ça reçup son action et ca execute le programme
    qui supprimera le contact dans la liste"""

    if request.form.get("supprimer"):
        liste_des_contact.pop(int(request.form.get("compteur")))
        ecriture_csv(liste_des_contact, "liste_des_contactes.csv", ";")
        lecture_csv("liste_des_contactes.csv", ";")
        return redirect ('/contact.html')


@app.route('/trier', methods= ['POST'])
def trier():
    if request.form.get('trier'):
        nvx_lst.clear()
        nvx_lst.append(sorted(liste_des_contact, key = tri))
        liste_des_contact.clear()
        for elem in nvx_lst[0]:
            liste_des_contact.append(elem)
        ecriture_csv(liste_des_contact, "liste_des_contactes.csv", ";")
        lecture_csv("liste_des_contactes.csv", ";")
        return redirect ('/contact.html')


@app.route('/share', methods= ['POST'])
def partage():
    """Quand l'utilisateur va appuyer sur partager, la fonction vcard est appeler avec les info de
    l'utilisateur"""
    if request.form.get('share'):
        contact_a_partager.append(liste_des_contact[int(request.form.get("compteur"))])
        vcard('Contacte.vcf', contact_a_partager)
        return redirect('/contact.html')
    
if __name__ == "__main__":
    app.run()  # Lance le serveur web