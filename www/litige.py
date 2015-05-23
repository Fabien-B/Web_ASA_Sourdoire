import mysql.connector

class Litige(object):
    database = 'asa'

    def __init__(self,id_lit,etat=None,id_rel1=None,id_rel2=None):
        if  id_lit>0:
            self.load(id_lit)
        else:
            connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
            curseur = connection.cursor()
            requete = 'select max(Id_Litige) from Litige;'
            curseur.execute(requete)
            (maxId,)=curseur.fetchall()[0]
            try :
                self.id = maxId + 1
            except TypeError:
                self.id = 1
            self.etat = etat
            self.id_rel1 = id_rel1
            self.id_rel2 = id_rel2

    def save(self):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = "INSERT INTO Litige VALUES ({0},{1},{2},{3});".format(self.id, self.etat, self.id_rel1, self.id_rel2)
        curseur.execute(requete)
        connection.commit()

    def load(self,id_lit):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = 'select * from Litige where Id_litige={};'.format(id_lit)
        curseur.execute(requete)
        try:
            (_,etat,id_rel1,id_rel2)=curseur.fetchall()[0]
        except IndexError:
            raise LitigeError("Litige with id {} doesn't exist".format(id_lit))

        self.etat = etat
        self.id_rel1 = id_rel1
        self.id_rel2 = id_rel2


class LitigeError(Exception):
    pass