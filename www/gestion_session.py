import mysql.connector
import bcrypt

def Connexion(page, choix, login='',password=''):
    if choix=='deconnecter':
        if "login" in Session(): del Session()["login"]
        return page('Deconnecte')
    else:
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = 'select login from Exploitant;'
        curseur.execute(requete)
        logins_tuples=curseur.fetchall()
        logins_list = []
        for (log,) in logins_tuples:
            logins_list.append(log)
        if not login in logins_list:
            return page('error')
        #else:
        requete = "select Password,Salt from Exploitant where login='{}';".format(login)
        curseur.execute(requete)
        (pw_base,salt)=curseur.fetchall()[0]
        pw_user = bcrypt.hashpw(password,salt)
        if pw_user == pw_base:
            Session()["login"] = login;
            return  page()
        else:
            return page('error')