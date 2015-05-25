import mysql.connector

class Releve(object):
    database = 'asa'

    def __init__(self,id_rel,compteur=None,exploitant=None,index_deb=None,index_fin=None,date=None):
        if  id_rel>0:
            self.load(id_rel)
        else:
            connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database=self.database)
            curseur = connection.cursor()
            requete = 'select max(Id_Releve) from Releve;'
            curseur.execute(requete)
            (maxId,) = curseur.fetchall()[0]
            self.id = maxId + 1
            self.compteur = compteur
            self.exploitant = exploitant
            self.index_deb = index_deb
            self.index_fin = index_fin
            self.date = date

    def save(self):
        if self.compteur == None or self.exploitant == None or self.index_deb == None or self.index_fin == None or self.date == None:
            raise ReleveError("All attributes must be completed")

        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database=self.database)
        curseur = connection.cursor()
        requete = "INSERT INTO Releve VALUES ({0},{1},{2},{3},{4},'{5}');".format(self.id, self.compteur, self.exploitant, self.index_deb, self.index_fin, self.date)
        curseur.execute(requete)
        connection.commit()

    def load(self,id_rel):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database=self.database)
        curseur = connection.cursor()
        requete = 'select * from Releve where Id_releve={};'.format(id_rel)
        curseur.execute(requete)
        try:
            (_,compteur,exploitant,index_deb,index_fin,date)=curseur.fetchall()[0]
        except IndexError:
            raise ReleveError("Releve with id {} doesn't exist".format(id_rel))

        self.id = id_rel
        self.compteur = compteur
        self.exploitant = exploitant
        self.index_deb = index_deb
        self.index_fin = index_fin
        self.date = date

    @staticmethod
    def get_releves_id(id_exploitant,youger_date=None, older_date=None):
        '''return a list of tuples: [(id_releve, id_parcelle), ... ]'''
        id_exploitant = int(id_exploitant)
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database=Releve.database)
        curseur = connection.cursor()

        if youger_date:
            youger_date = "'{}'".format(youger_date)
        else:
            youger_date = 'NULL'

        if older_date:
            older_date = "'{}'".format(older_date)
        else:
            older_date = 'NULL'

        if id_exploitant:
            requete = '''SELECT Releve.Id_releve,Parcelle.Id_parcelle FROM Releve,Parcelle,Propriete
                    WHERE Releve.Exploitant = {2}
                    AND Propriete.Id_exploitant = Releve.Exploitant
                    AND Releve.Compteur = Parcelle.Compteur
                    AND Parcelle.Id_parcelle = Propriete.Id_parcelle
                    AND (Propriete.date_debut < Releve.Date OR Propriete.date_debut IS NULL)
                    AND (Propriete.date_fin > Releve.Date OR Propriete.date_fin IS NULL)
                    AND (Releve.Date < {0} OR {0} IS NULL)
                    AND (Releve.Date > {1} OR {1} IS NULL)
                    ORDER BY Releve.Date;'''.format(older_date,youger_date,id_exploitant)
        else:
            requete = '''SELECT Id_releve,-1 FROM Releve
                    WHERE Releve.Exploitant = {2}
                    AND (Releve.Date < {0} OR {0} IS NULL)
                    AND (Releve.Date > {1} OR {1} IS NULL)
                    ORDER BY Releve.Date;'''.format(older_date,youger_date,id_exploitant)
        curseur.execute(requete)
        id_rel_tuple = curseur.fetchall()
        id_rel_list = []
        for (id_rel,id_pacelle) in id_rel_tuple:
            id_rel_list.append((id_rel,id_pacelle))

        return id_rel_list

class ReleveError(Exception):
    pass
#                    'AND Id_exploitant={2}'